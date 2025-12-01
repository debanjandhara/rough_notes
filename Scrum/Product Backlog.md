Here is the **Product Backlog** formatted for Excel.

**Logic Applied:**
*   **Actual Sprint:** Indicates which sprint the story was allocated to based on the dependency flow (e.g., Search cannot happen before Posts exist).
*   **MoSCoW:** Based on the "Priority" section in your provided Epic/User Stories.
*   **Dependency:** Shows logical technical constraints.
*   **Status:** "Completed" implies the project is finished (Day 14). "Descoped" items are those listed as "Won't Have" or "Could Have" features that didn't fit the 10-day timeline.

### Product Backlog

| Actual Sprint | UserStory ID | User Story Description | MoSCoW | Dependency | Assignee | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Sprint 1** | **US-0** | **Authentication:** As a user, I need to register, login, and have my session managed securely (JWT/Cookies). | **MUST** | None | Shreya | Completed |
| **Sprint 1** | **US-1** | **Create/Publish Posts:** As a blogger, I should be able to create posts with a rich text editor and multimedia. | **MUST** | US-0 (Auth) | Rakshita / Debanjan | Completed |
| **Sprint 1** | **US-2** | **Taxonomy:** As a blogger, I should be able to manage categories and tags for my blog posts. | **MUST** | None | Anu | Completed |
| **Sprint 1** | **US-5** | **Theming (Basic):** As a blogger, I want to choose basic colors and fonts to customize my blog's look. | **MUST** | None | Maha | Completed |
| **Sprint 1** | **US-1.1** | **Post Scheduling:** As a blogger, I want to schedule posts for a future date (Cron jobs). | **SHOULD** | US-1 | Debanjan | Completed |
| **Sprint 2** | **US-3** | **Search & Filter:** As a reader, I should be able to search posts by keywords, categories, and tags. | **MUST** | US-1, US-2 | Anu | Completed |
| **Sprint 2** | **US-4** | **Comments:** As a reader, I want to comment on posts; As a blogger, I want to moderate them. | **MUST** | US-0, US-1 | Rakshita | Completed |
| **Sprint 2** | **US-7** | **Analytics:** As a blogger, I should be able to track my blog's performance (Views/Likes). | **SHOULD** | US-1 | Maha | Completed |
| **Sprint 2** | **US-6** | **Social Media:** As a blogger, I should be able to connect accounts and share content links. | **COULD** | US-0 | Shreya | Completed |
| **Sprint 2** | **US-5.1** | **Advanced Theming:** Upload custom logos and import/export design settings. | **COULD** | US-5 | Maha | Descoped |
| **Sprint 2** | **US-7.1** | **Competitor Analysis:** Compare blog performance with competitors. | **WONT** | US-7 | Maha | Descoped |
| **Sprint 2** | **US-4.1** | **Comment Reporting:** Option for readers to report inappropriate comments. | **WONT** | US-4 | Rakshita | Descoped |
