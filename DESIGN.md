# DESIGN.md: Akershus Festning — Mulighetsstudie

## Source

- URL: https://www.akershusfestning.info/
- Capture date: 2026-08-28
- Stack detected: Next.js + Tailwind CSS (purged build), react-modal
- Evidence used:
  - `branding` + `images` scrape of `/` and `/potensial` (Firecrawl)
  - Full CSS bundle `/_next/static/css/39240b6d8c06713a43a2.css` (fetched directly — the authoritative token source)
  - Rendered HTML fragment of `/` (component class chains)
  - Page markdown of `/` (51 KB narrative, caption/credit conventions)
  - Viewport screenshots of `/`, `/potensial`, `/intro` (some via scripted scroll/click actions)

> Credits, logo, photography and copy belong to Forsvarets museer / Freeman Ryan Design / TRY. This file documents the **design language** only. Do not reuse the wordmark, the archival images, or the Norwegian copy.

### Capture caveats

- `/` is gated by a first-visit welcome modal. The first `branding` pass read the modal, not the page, and reported a flat `h1/h2/body = 16px`. **Discard that.** The type scale below comes from the CSS bundle and from an interior route (`/potensial`) that rendered ungated.
- The site is a scroll-driven narrative. `document.body.scrollHeight` is short and sections are pinned, so full-page screenshots come back mostly blank and programmatic scrolling jumps to the closing block. Viewport captures at known routes are the reliable visual evidence.

## Reference Screenshots

![Interior chapter, /potensial — full-bleed archival photography, caption/credit block, right nav rail](./.firecrawl/akershus-potensial.png)

![Welcome gate modal over the video hero on /](./.firecrawl/akershus-screenshot.png)

Use the first screenshot as the visual source of truth for layout, density and hierarchy. Tokens below describe the same system in machine-readable form.

> These assets live in `.firecrawl/`, which is gitignored. They are a local cache — move them into a tracked folder if this file needs to travel.

## Design Summary

A red-on-white museum monograph that behaves like a scrolling exhibition. The page gives almost all of its area to full-bleed archival photography — mostly black-and-white, edge-to-edge, no rounded corners, no cards, no borders — and reserves a single saturated red (`#DF1B12`) for every piece of interface: the wordmark, the nav, the captions, the credits, the icons, the one button. Body copy is black, set large (about 30px) in a geometric sans with generous leading. Chrome is minimal and floats: a fixed transparent header with a centered wordmark, and a right-hand vertical table of contents whose labels fade in only on hover or when active.

Type does the dramatic work. Narrative beats are single fragmentary words — *Krig*, *død*, *fest*, *monarki* — set in viewport-relative sizes up to `24vw`, and years are set at `12.5vw` with a `0.79` line-height. Occasional interludes invert to a fixed radial gradient from deep royal red to black.

The tone is institutional and reverent, never playful: no gradients on buttons, no shadows except one soft modal shadow, no decorative shapes. Restraint plus scale is the whole idea.

## Design Tokens

### Colors

All values observed directly in the CSS bundle unless marked inferred.

| Role | Token | Value | Usage |
|---|---|---|---|
| Brand primary | `red` | `#DF1B12` | Wordmark, nav, captions, icons, primary button, headings on light |
| Emphasis / link | `signal-red` | `#FF4A4A` | Links; the brighter red that survives dark grounds |
| Dark ground base | `royal-red` | `#50121F` | Center of the dark-section gradient |
| Dark ground mid | *(gradient stop)* | `#280910` | Gradient midpoint, no utility class |
| Ink | `black` | `#000000` | Body copy on light |
| Ground | `white` | `#FFFFFF` | Default page background |
| Warm light | `light-beige` | `#FBF1E4` | Alternate light ground |
| Warm accent | `beige` | `#F4D1A8` | Text accent on dark grounds |
| Muted | `gray-400` | `#9CA3AF` | Secondary/disabled text (inferred: Tailwind default, reported by branding pass) |

Dark section background, verbatim:

```css
.dark {
  background: radial-gradient(82.65% 50% at 50% 50%,
              #50121f 5.65%, #280910 68.73%, #000 100%) #000 50% no-repeat;
  background-attachment: fixed;
  background-size: cover;
}
```

`background-attachment: fixed` is deliberate: the glow stays put while content scrolls over it.

Focus ring: `ring-yellow-50` at 25% opacity — a warm, near-invisible halo rather than a browser default.

### Typography

Two self-hosted commercial families. **Neither is on Google Fonts**, and both are served as raw `.otf` from `/fonts/` — you cannot reuse the files, so any rebuild needs licensed originals or the substitutes below.

| Role | Family | Weights shipped | Fallback stack |
|---|---|---|---|
| Body / UI | CeraPro | 300, 400, 500, 700 | `"Cera Pro", Poppins, Montserrat, ui-sans-serif, system-ui, sans-serif` (geometric grotesque, single-storey `a`) |
| Display serif | Glysa | 400 only | `Glysa, "Playfair Display", Prata, Georgia, serif` (high-contrast display serif) |

Root: `html { font-family: CeraPro, sans-serif; line-height: 1.5 }`. Serif is opt-in via `.font-serif` and used sparingly.

Type scale, exactly as defined in the bundle:

| Token | Size | Line height | Role |
|---|---|---|---|
| `text-screen-xxl` | `24vw` | — | Single-word narrative beat, largest |
| `text-screen-lg` | `18vw` | — | Narrative beat |
| `text-number` | `12.5vw` | `0.79` | Timeline years (`1300`, `1905`…) |
| `text-screen-md` | `11vw` | — | Narrative beat, smaller |
| `text-h2` | `3rem` (48px) | `1.5` | Section heading |
| `text-5xl` | `3rem` | `1` | Display heading, tight |
| `text-4xl` | `2.25rem` | `2.5rem` | |
| `text-h3` | `2rem` (32px) | `1.5` | Subsection heading |
| `text-3xl` | `1.875rem` | `2.25rem` | |
| `text-2xl` | `1.5rem` | `2rem` | |
| `text-lead` | `1.5rem` (24px) | `1.375` | Lead paragraph |
| `text-xl` | `1.25rem` | `1.75rem` | |
| `text-lg` | `1.125rem` | `1.75rem` | |
| `text-base` | `1rem` | `1.5rem` | |
| `text-sm` | `0.875rem` | `1.25rem` | Buttons, captions, credits |
| *(nav link)* | `12px` | — | `font-weight: 400`, `text-transform: uppercase` |

Rendered measurements on `/potensial` at 1920px: **h1 ≈ 104px, h2 ≈ 48px, body ≈ 30px**. Body copy is deliberately oversized — treat ~28–30px as the reading size at desktop, not 16px.

The `vw` tiers are the signature. Do not substitute fixed `rem` sizes for them; the headline is meant to bleed to the viewport edges at every width.

### Spacing And Layout

- Base unit: **4px** (standard Tailwind scale).
- Breakpoints: `sm 640` · `md 768` · `lg 1024` · `xl 1280` (the only widths present as `@media` rules in the bundle; `2xl 1536` exists as a container utility only — inferred as Tailwind default). The `xl` (1280) breakpoint is the meaningful one — it switches the nav from full-screen overlay to persistent right rail.
- Containers: `max-w-screen-{sm,md,lg,xl,2xl}`, plus `max-w-4xl` (56rem) and `max-w-lg` (32rem) for text measure. Media is **not** contained — it runs full-bleed.
- Header padding: `p-4` mobile, `md:px-12`. Nav padding: `p-7 pb-24 xl:pb-7`.
- Radii: `rounded-md 0.375rem` (buttons, modal — the default), `rounded-lg 0.5rem`, `rounded-xl 0.75rem`, `rounded-full` (icon hit areas). **Images and sections are square-cornered.**
- Shadows: exactly one, `shadow-modal: 0px 4px 42px -4px rgba(0,0,0,0.25)`. Nothing else casts a shadow.
- Borders: `border-red` only. No neutral dividers; separation comes from whitespace and from image edges.

### Motion

- Durations: `150ms` default, `300ms`, `500ms` (nav label fades). Easing: `cubic-bezier(0.4, 0, 0.2, 1)` throughout.
- Header uses `transition-colors duration-150` — the wordmark and icons recolor as the header crosses light and dark sections (inferred from the class chain plus observed light/dark grounds).
- Nav labels animate opacity only: `0` at rest → `0.7` on hover → `1` when active, over `500ms`. The dash rule beside each item stays visible.
- No transforms, parallax libraries, or entrance animations detectable in CSS; the drama is scroll position plus type scale.

## Components

**Header** — fixed, `z-30`, full width, transparent over media.
```html
<header class="main-header text-red flex items-center p-4 md:px-12 fixed top-0 left-0 right-0 z-30 duration-150 transition-colors">
  <a class="main-logo mx-auto relative h-12 md:h-14" href="/"></a>
  <!-- utility icons, right -->
</header>
```
Wordmark centered via `mx-auto`, 48px tall (56px from `md`). Utility icons sit at the right: download report, sound toggle, help — 24px SVG, `stroke-width: 2`, `stroke="currentColor"`, round caps/joins, `title` attributes in the site language.

**Nav rail (table of contents)** — fixed, full viewport height, right-aligned column.
```html
<nav class="h-screen fixed flex flex-col items-end right-0 left-0 xl:left-auto top-0
            p-7 pb-24 xl:pb-7 pointer-events-none bg-opacity-90 xl:bg-transparent">
```
Each item: uppercase 12px red label, then a short horizontal rule to its right. At rest only the rules show; labels fade in on hover, and the active chapter stays at full opacity with a longer rule. Below `xl` it collapses behind a hamburger (`title="Hovedmeny"`) into a 90%-opacity full-screen overlay. `pointer-events-none` on the container with `pointer-events-auto` on children keeps the rail from blocking the imagery.

**Welcome gate modal** — react-modal, white panel centered over the dimmed video hero, `shadow-modal`, `rounded-md`. Structure: centered wordmark → red heading → two body paragraphs (`mb-8`) → primary button → secondary text link with an external-link glyph. Close button:
```html
<button aria-label="Lukk modalvindu"
        class="absolute top-2 right-2 md:top-8 md:right-8 focus:outline-none focus:ring ring-yellow-50 ring-opacity-25 text-red">
```

**Primary button** — the only button style on the site.
```html
<button class="mb-4 bg-red text-white p-4 py-3 text-sm font-medium rounded-md
               focus:outline-none focus:ring ring-yellow-50 ring-opacity-25">
```
Solid `#DF1B12`, white 14px medium, 16px horizontal / 12px vertical padding, 6px radius, no shadow, no gradient. A download variant prefixes the 24px download icon inside the same pill.

**Full-bleed media + caption block** — the workhorse. Image spans the full viewport width at roughly 80–85% viewport height, square corners, no frame. Directly beneath, right-aligned:

```
Akershus festning, 1907        ← bold, red, text-sm
Fotograf: Anders Beer Wilse.   ← regular, red, text-sm
Oslo Museum.                   ← regular, red, text-sm
```

Title in bold red, then medium and attribution, then holding institution, each on its own line. This caption-plus-credit convention appears on essentially every image and is the strongest single signal of the site's museum register — reproduce it, not just the tokens.

**Narrative beat** — one fragment of a sentence per scroll step (`Krig`, `død`, `fest`, `monarki`, `Norges`, `historie`), set in `text-screen-*`, centered, over white or over the `.dark` gradient. Consecutive beats complete one sentence across several viewports.

**Timeline numeral** — a bare year in `text-number` (`12.5vw`, line-height `0.79`) anchoring a historical section.

**Scroll affordance** — centered, uppercase red `SCROLL` in small type above a thin chevron, at the base of the first viewport.

**Closing / contact block** — red two-line heading at ~36px, black body copy in a plain stacked list (role, then contact lines), with the red download button centered above. No footer bar, no link farm, no social icons.

## Page Patterns

Nine routes, one per chapter, each a self-contained scroll narrative:
`/` · `/intro` · `/potensial` · `/en-ny-besoksopplevelse` · `/forsvarsmuseum` · `/kulturfestning` · `/oscarsborg` · `/overordnet-strategi` · `/oppsummering`

Chapter rhythm:

1. Full-bleed hero image or looping video, wordmark floating over it, `SCROLL` cue.
2. Alternating steps: full-bleed image with caption/credit → short body column (left-aligned, roughly half width, oversized copy) → narrative beat in `vw` type.
3. Occasional dark interlude on the fixed radial gradient, type reversed to white / `beige` / `signal-red`.
4. Timeline numerals for historical passages.
5. Closing contact block plus report download.

Responsive behaviour:
- Below `xl`, nav rail → hamburger overlay; header padding drops to `p-4`; the wordmark shrinks to `h-12`.
- `vw` type keeps its proportions at every width, so headline drama survives on mobile without breakpoint-specific sizes.
- Media stays full-bleed at all widths; only the text column is constrained.

## Content Style

- Fragmentary, cinematic headings. Sentences are split across scroll steps and finished several viewports later. Single evocative nouns carry whole screens.
- Sentence case, no exclamation marks, no marketing superlatives. Institutional and calm.
- Body paragraphs are short — three or four lines at the site's large reading size.
- Every image is attributed. Bold title line, then `Fotograf:` / `Fotografi:` / `Oljemaleri:` / `Litografi:` plus name, then the holding institution. Unknown photographers are stated as unknown rather than omitted.
- CTAs are plain imperatives naming the object: *Continue to the feasibility study*, *Download the feasibility study*. No "Learn more", no "Get started".
- Nav labels are uppercase noun phrases.
- Persistent affordances are described in-page (a short "Menu" explainer tells the reader the rail is the table of contents) — the site teaches its own interaction rather than assuming it.

## Agent Build Instructions

1. **Tailwind config.** Extend rather than replace:
   ```js
   theme: {
     extend: {
       colors: {
         red: '#DF1B12',
         'signal-red': '#FF4A4A',
         'royal-red': '#50121F',
         'light-beige': '#FBF1E4',
         beige: '#F4D1A8',
       },
       fontFamily: {
         sans: ['CeraPro', 'Poppins', 'ui-sans-serif', 'system-ui', 'sans-serif'],
         serif: ['Glysa', '"Playfair Display"', 'Georgia', 'serif'],
       },
       fontSize: {
         lead: ['1.5rem', { lineHeight: '1.375' }],
         h3: ['2rem', { lineHeight: '1.5' }],
         h2: ['3rem', { lineHeight: '1.5' }],
         'screen-md': '11vw',
         'screen-lg': '18vw',
         'screen-xxl': '24vw',
         number: ['12.5vw', { lineHeight: '0.79' }],
       },
       boxShadow: { modal: '0px 4px 42px -4px rgba(0,0,0,0.25)' },
     }
   }
   ```
2. **Fonts.** Substitute the fallbacks above unless licences for Cera Pro and Glysa are in hand. Keep exactly two families: one geometric sans carrying everything, one display serif used rarely.
3. **Discipline to hold.** One red for all interface. Square corners on media, 6px radius on controls only. One shadow, on the modal. No cards, no neutral dividers, no icon decoration beyond the three utility glyphs.
4. **Set body copy at 28–30px desktop** with `line-height: 1.5` and constrain the text column to roughly `max-w-4xl` while media runs full-bleed.
5. **Build the scroll narrative first, tokens second.** Structure each chapter as alternating full-bleed image steps and short text columns, with `vw`-sized single-word beats between them. Without that rhythm the palette alone reads as a generic red-and-white site.
6. **Chrome floats, never boxes.** Fixed transparent header with a centered wordmark, `z-30`, `transition-colors duration-150` so it recolors across light and dark sections. Right rail with `pointer-events-none` on the container.
7. **Image delivery.** The source serves responsive sources at `w=1920`, `2048` and `3840` with `q=75`. For full-bleed photography at this scale, ship up to 3840w and hold quality around 75 — the imagery is the product, and undersized sources are the first thing that breaks the effect.
8. **Caption every image** with the bold-title-then-credit pattern, right-aligned under the media.
9. **Accessibility to fix, not copy.** The source has real gaps worth correcting in any rebuild: `#DF1B12` on white measures 4.88:1 — it clears AA for normal text by a hair but fails AAA, and it is used at 12–14px for nav and credits; `#FF4A4A` on white measures 3.32:1, which fails AA for body text and only passes as large text. Nav labels sit at `opacity: 0` until hover, invisible to sighted keyboard users. The `vw` type has no `clamp()` floor or ceiling. In a rebuild: darken or enlarge the credit red, reserve `signal-red` for dark grounds only (it measures 6.33:1 on black), keep focus-visible labels at full opacity, and bound the `vw` sizes with `clamp()`.
10. **Localise the register, not the language.** The Norwegian copy is specific to this project; what transfers is the archival-attribution habit and the fragmentary heading cadence.

## Rerun Inputs

```
workflow: firecrawl-website-design-clone
source_url: https://www.akershusfestning.info/
target_stack: Tailwind CSS (framework-agnostic tokens)
output: DESIGN.md
```
