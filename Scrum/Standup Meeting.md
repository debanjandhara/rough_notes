Here is the **Daily Standup Sheet** designed to accompany the Scrum Sheet. It reflects the natural progression of the project, highlighting specific "human" errors, technical blockers (CORS, Merge Conflicts, API mismatches), and the actions taken to resolve them during the 10-day development cycle.

### Standup Meeting Log

| Sprint No | Day | Date | Team Member | Impediments / Blockers | Action Taken |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Sprint 1** | **Day 1** | **18-Nov** | Debanjan | MongoDB Atlas connection string is throwing generic network errors for the team. | Updated `env.js` template with correct whitelist IP settings and reshared `.env` file. |
| | | | Maha | Unsure if we should use a global CSS file or Tailwind config for the dynamic theme switching. | **Decision:** We will use `ThemeContext` to inject CSS variables, but keep Tailwind for layout. |
| **Sprint 1** | **Day 2** | **19-Nov** | Rakshita | Struggling with Tiptap Editor library; the "Video Node" extension is crashing the build. | **Pair Programming:** Debanjan will join Rakshita post-standup to debug the custom node implementation. |
| | | | Anu | Multer upload logic is confusing; not sure where to store temp files before cloud upload. | Clarified that for this MVP, we will store locally in `public/uploads` first to save time. |
| **Sprint 1** | **Day 3** | **20-Nov** | Shreya | Frontend Auth UI is ready, but I don't know the exact error codes the Backend sends (e.g., 401 vs 403). | Shreya and Debanjan to sync for 15 mins to document standardized API error responses. |
| | | | Maha | `GlassCard` component transparency looks different on Firefox vs Chrome. | Added specific vendor prefixes (`-webkit-backdrop-filter`) to `index.css`. |
| **Sprint 1** | **Day 4** | **21-Nov** | **ALL** | **BLOCKER:** Frontend cannot talk to Backend. CORS (Cross-Origin Resource Sharing) errors on all browsers. | Debanjan installed `cors` package in Express and whitelisted the Vite localhost port (5173). |
| | | | Anu | The "Tags" input allows duplicates if the casing is different (e.g., "Tech" vs "tech"). | Added a `.toLowerCase()` normalization step in the `tag.controller.js` before saving. |
| **Sprint 1** | **Day 5** | **22-Nov** | Rakshita | **Merge Conflict:** My dashboard layout changes conflict heavily with Maha's Navbar updates in `App.jsx`. | **Code Freeze:** Stopped new commits. Team did a screen-share session to resolve git conflicts line-by-line. |
| | | | Shreya | Unit tests for "Forgot Password" are failing because we don't have a real email server. | Mocked the email service in the test environment so we don't need real SMTP credentials yet. |
| | | | | | |
| **Sprint 2** | **Day 6** | **25-Nov** | Anu | The search requirement is vague. Should it be exact match or fuzzy search? | **Decision:** We will use MongoDB `$regex` for partial matching on titles and tags for now. |
| | | | Maha | The Analytics API returns data in an object format, but the Recharts library needs an Array. | Maha will write a utility function in `utils.js` to transform the data shape on the client side. |
| **Sprint 2** | **Day 7** | **26-Nov** | Rakshita | The comment section doesn't update immediately after posting; user has to refresh. | Added `useBlogData` context refresh trigger to re-fetch comments upon successful submission. |
| | | | Debanjan | Deployment script on Render is failing; it can't find the `models` folder. | **Fix:** Fixed case-sensitivity issue (folder was named `Models` locally but git pushed as `models`). |
| **Sprint 2** | **Day 8** | **27-Nov** | Anu | **Performance:** The search bar makes an API call on every single keystroke, freezing the UI. | **Action:** Implemented `lodash.debounce` with a 500ms delay to reduce API load. |
| | | | Shreya | "Admin Delete User" works, but their blog posts remain in the database as orphans. | Updated `user.controller.js` to cascade delete posts (or set author to null) when a user is deleted. |
| **Sprint 2** | **Day 9** | **28-Nov** | Maha | Google Fonts API is loading too slowly, causing "Flash of Unstyled Text" (FOUT). | Switched to pre-loading only the top 3 popular fonts and letting others lazy load. |
| | | | Rakshita | Moderate Comments button is visible to normal users in the API response (security risk). | Updated backend `comment.controller` to only send moderation flags if `req.user.role === 'admin'`. |
| **Sprint 2** | **Day 10** | **29-Nov** | **ALL** | Final Build size is too large (vendor chunk is 2MB+). | Debanjan configured Vite `rollupOptions` to split chunks (lazy load Tiptap and Recharts). |
| | | | All Team | Preparing for Demo. Found a bug where the "Logout" button sometimes doesn't clear the cookie. | **Hotfix:** Added a `clearCookie` instruction with specific path options in the `auth.controller` logout method. |
