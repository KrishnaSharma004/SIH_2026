# Urban IQ Dashboard — Codebase & UI Reference

A quick-reference doc for the B2 frontend: what each file does, how data flows, and what every UI element on screen actually means.

---

## 1. What this app is

A React + Leaflet dashboard that displays detection and incident data collected by the bus fleet's edge AI (A1/A2's work). It reads from an API — right now a mock one (`mock-api/`), later B1's real backend — and shows it as a live map, heatmaps, incident evidence pages, and an admin table.

---

## 2. Folder structure

```
dashboard/
├── index.html          entry HTML — loads Leaflet's CSS, mounts React at #root
├── vite.config.js       build tool config (nothing to touch normally)
├── package.json         dependencies + npm scripts
└── src/
    ├── main.jsx          bootstraps React + routing
    ├── App.jsx            top nav + page routes
    ├── index.css          all styling (dark theme)
    ├── api/
    │   └── client.js      the ONE place the API base URL lives
    ├── components/
    │   └── LoadingState.jsx   shared loading/error UI
    └── pages/
        ├── LiveTracking.jsx    map with live detection markers
        ├── HeatmapView.jsx     heatmap layer with type toggle
        ├── IncidentDetail.jsx  single incident's evidence + work-order button
        └── AdminPanel.jsx      filterable table of all records

mock-api/
├── package.json         runs json-server
└── db.json               fake detections/incidents/heatmap data (matches the real API's shape)
```

---

## 3. File-by-file: what each one does

| File | Purpose |
|---|---|
| `main.jsx` | Wraps the app in `<BrowserRouter>` and renders it into the page. You almost never edit this. |
| `App.jsx` | Defines the top nav bar and which page shows for which URL (`/`, `/heatmap`, `/incidents/:id`, `/admin`). |
| `api/client.js` | A single `axios` instance pointed at the API base URL. Every page imports this instead of calling `axios` directly — so switching from mock data to B1's real backend is a one-line change here, nowhere else. |
| `components/LoadingState.jsx` | Two tiny components (`LoadingState`, `ErrorState`) reused across every page so "loading…" and "error" look consistent everywhere. |
| `pages/LiveTracking.jsx` | Fetches `/detections`, drops a pin per record on the map. |
| `pages/HeatmapView.jsx` | Fetches `/heatmap?type=X`, renders it as a density heat layer. Has its own small `HeatLayer` helper component because `react-leaflet` doesn't support heatmaps natively — this wires in the `leaflet.heat` plugin. |
| `pages/IncidentDetail.jsx` | Fetches one incident by ID from the URL, shows its evidence, and can POST a new work order. |
| `pages/AdminPanel.jsx` | Fetches all detections into a filterable table — the "for city staff" view. |
| `index.css` | All visual styling. Uses CSS variables (`--bg`, `--surface`, `--accent`, etc.) at the top so the whole theme can be recolored by editing one block. |
| `mock-api/db.json` | Stand-in data. Its shape (field names, types) is the contract the real backend must also follow. |

---

## 4. How data flows

```
mock-api (or B1's real API)
        │  GET /detections, /incidents/:id, /heatmap
        ▼
  src/api/client.js
        │
        ▼
  a page component (LiveTracking, HeatmapView, IncidentDetail, AdminPanel)
        │  useState + useEffect: fetch on load, store in state
        ▼
  rendered UI (map markers / heat layer / table rows / detail card)
```

Every page follows the same pattern: fetch on mount → show `LoadingState` while waiting → show `ErrorState` on failure → render the real content once data arrives. If you understand `LiveTracking.jsx`, you understand the shape of all four pages.

---

## 5. What each part of the UI means

### Top navigation bar
Three links — **Live Tracking**, **Heatmap**, **Admin** — switch between the three main views. The currently active link is highlighted (styled via the `.active` class React Router adds automatically).

### Live Tracking screen
- **Map markers** — each pin is one detection event. Clicking a pin opens a popup showing its **type** (pothole, waterlogging, etc.), **confidence score** (how sure the model was), and which **bus/route** reported it.
- **"View incident" link** — only appears on markers whose type is `incident`; takes you to that incident's detail page.

### Heatmap screen
- **Toggle buttons** (`pothole` / `congestion` / `waterlogging`) — switch which detection type the heatmap visualizes. Only one is active at a time.
- **Heat layer** — warmer/denser areas mean more detections of that type clustered there; this is what would drive the "infrastructure deficiency" and "congestion hotspot" insights from the architecture doc.

### Incident detail screen
- **Type** — the incident category (e.g. hit-and-run).
- **Plate** — the ANPR-read registration number.
- **Confidence** — how reliable that plate reading is; low confidence should get flagged for human review in a real deployment.
- **Timestamp / Location** — when and where it happened.
- **Evidence image** — the frame captured at detection time, for verification.
- **"Create work order" button** — simulates notifying an authority; on click it POSTs to the mock backend and the button updates to a confirmed state.

### Admin panel
- **Filter buttons** — one per detection type found in the data, plus "all". Narrows the table to just that type.
- **Table rows** — one row per record; the rightmost column links to the incident detail page for any row that is an incident, otherwise it's blank (a pothole/road-defect record has no separate detail page in this build).

---

## 6. The one thing to remember when extending this

Every new page or feature should follow the existing pattern: put API calls through `api/client.js`, use `LoadingState`/`ErrorState` for the fetch lifecycle, and keep new screens under `src/pages/`. That consistency is what makes it easy for a second person (or future you) to read any file in this repo without a walkthrough.
