# Box Box - Live F1 Minimap & Telemetry Dashboard

**Box Box** is a real-time Formula 1 dashboard that visualizes live session telemetry and reconstructs actual track layouts using raw location coordinate feeds from the open-source **OpenF1 API**. 

Built using **Svelte 5 (Runes)** for high-performance 60fps UI rendering and **Tailwind CSS v4** for modern, glassmorphic dark-mode aesthetics.

---

## Key Features

* **Dynamic Track Reconstruction:** Dynamically parses 3D Cartesian coordinates (`x`, `y`) from a single driver's lap to draw any F1 circuit perfectly as scalable vector graphics (SVG).
* **Live Driver Minimap Tracker:** Animates all active driver dots moving smoothly around the vector circuit layout in real-time.
* **60fps Interpolation Loop:** Employs Linear Interpolation (Lerp) to smooth out driver coordinate signals (~3.7 Hz API sampling rate) for lag-free, fluid motion.
* **Active Telemetry HUD:** Click any driver to load real-time car metrics including current Speed (km/h), engine RPM, Gear Selection, Throttle, and Brake inputs.
* **Session Picker:** Explore active and historical sessions directly from the official OpenF1 session registry.

---

## Technology Stack

* **Frontend Framework:** [Svelte 5](https://svelte.dev/) (utilizing modern reactive `$state`, `$derived`, and `$effect` runes)
* **Build System:** [Vite 8](https://vite.dev/)
* **CSS Framework:** [Tailwind CSS v4](https://tailwindcss.com/) (CSS-first engine)
* **Data Provider:** [OpenF1 REST API](https://openf1.org/) (CORS-enabled public endpoint)

---

## Technical & Mathematical Implementation

### 1. Circuit Vector Mapping (Scaling & Translation)
Formula 1 cars transmit their location coordinates in a Cartesian system ($x, y, z$) representing decimeter/meter offsets from a track-specific origin. To translate these arbitrary values onto a scalable web browser SVG canvas:

1. Let $\mathbf{P} = \{(x_1, y_1), (x_2, y_2), ..., (x_n, y_n)\}$ be the set of coordinates representing a single completed lap.
2. Find the bounding box boundaries:
   $$X_{min} = \min(X), \quad X_{max} = \max(X)$$
   $$Y_{min} = \min(Y), \quad Y_{max} = \max(Y)$$
3. Compute the viewport width ($W$) and height ($H$):
   $$W = X_{max} - X_{min}, \quad H = Y_{max} - Y_{min}$$
4. Calculate the scaled coordinates to draw the SVG vector path:
   $$\text{Screen } X = x_i - X_{min}$$
   $$\text{Screen } Y = Y_{max} - y_i$$
   *(Note: The $Y$ coordinate is inverted because SVG vertical space increases downwards, whereas track coordinates increase upwards).*

### 2. Smooth Linear Interpolation (Lerp)
To prevent the driver indicators from jumping or stuttering between the API's $3.7\text{ Hz}$ update ticks:
* We track the driver's current screen position $\mathbf{P}_{current}$ and their incoming target position $\mathbf{P}_{target}$.
* On every screen redraw (`requestAnimationFrame` at 60fps), we calculate the next transition step:
  $$\mathbf{P}_{current} = \mathbf{P}_{current} + (\mathbf{P}_{target} - \mathbf{P}_{current}) \times \alpha$$
  *(where $\alpha \approx 0.1$ behaves as a smooth easing coefficient).*

---

## Getting Started

### Prerequisites
Make sure you have [Node.js](https://nodejs.org/) installed on your machine.

### Installation & Setup

1. **Clone or Navigate to the Directory:**
   ```bash
   cd BoxBox
   ```

2. **Install Node Packages:**
   ```bash
   npm install
   ```

3. **Boot up the Local Development Server:**
   ```bash
   npm run dev
   ```

4. Open the development link shown in your terminal (typically `http://localhost:5173`) inside your web browser.

---

## Project Architecture

```
BoxBox/
├── src/
│   ├── assets/           # Dynamic icons, team badges, SVGs
│   ├── components/       # Custom modular components
│   │   ├── TrackMap.svelte      # Canvas/SVG layout drawer
│   │   ├── TelemetryHUD.svelte  # Speedometer and telemetry gauges
│   │   └── Leaderboard.svelte   # Live driver list & gaps
│   ├── App.svelte        # Main layout, orchestrates global states
│   ├── app.css           # Tailwind v4 import entry
│   └── main.js           # Mounts the Svelte 5 application
├── index.html            # Main HTML document template
├── vite.config.js        # Vite build configurations with Tailwind v4
└── package.json          # Node scripts and dependencies
```
