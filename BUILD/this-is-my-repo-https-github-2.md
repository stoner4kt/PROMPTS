# This is my repo https://github

This is my repo https://github.com/stoner4kt/ToursystemV2refactored/tree/main analyze it. It's a system for a Tour Fleet. I want to ensure that the Ui&UX looks professional on all mobile and Desktop screens and user experience is excellent. There are areas in the system where on mobile as screens and even some larger screens where tables span of the screen (some data is not displaying because it's displayed off the screen). Goal: I am building a web application (an admin dashboard named "INYATHI Admin Dashboard") and the layout is currently breaking on mobile viewports. It is not responsive, elements are squeezed, and the browser is force-zooming out to make things fit, making it look unprofessional. 

I have attached screenshots of the issues:
1. "Screenshot_20260628_174119_com.huawei.browser.jpg" and "Screenshot_20260628_174127_com.huawei.browser.jpg" show the fixed-width sidebar crushing the layout on mobile.
2. "Screenshot_20260628_174309_com.huawei.browser.jpg" and "Screenshot_20260628_174333_com.huawei.browser.jpg" show a mobile desktop browser rendering things microscopically, where side-by-side elements (Forms and Tables) are clipped off-screen with no horizontal scrolling capability.

I need you to analyze my repository/code snippets and provide the exact layout refactoring required to make this dashboard look clean, professional, and fully responsive across mobile, tablets, and laptops.

Please implement the following specific architectural and styling fixes using Tailwind CSS:

1. **Meta Viewport Tag:** Ensure the application has the correct `<meta name="viewport" content="width=device-width, initial-scale=1.0">` tag configured in the root layout or document wrapper.
2. **Responsive Sidebar:** Convert the static sidebar layout into a responsive shell. On mobile/tablet viewports, the sidebar must be hidden by default (or slide out as a drawer/drawer menu) toggled via a hamburger button in the top navigation bar. On desktop/laptops, it should remain pinned to the left side as it currently is.
3. **Responsive Top Navbar Real Estate:** Optimize the top header items (such as the "Cape Town / Joburg" city selectors). On mobile screens, consider converting this into a compact dropdown menu or an icon-based toggle to save precious top-bar real estate.
4. **Responsive Grid/Flex Overhaul:** Change side-by-side elements (like the "Generate Driver Signup Invite" form and the "Driver Details" table) to stack vertically using `flex-col` on mobile and transition to `lg:flex-row` on larger screens.
5. **Scrollable Data Tables:** Ensure all main wrappers or table wrappers have Tailwind's `overflow-x-auto` class (combined with a parent element using `min-w-0` if inside a flex container). This must allow mobile users to smoothly scroll horizontally just the table data without breaking the layout of the entire app or clipping the text off-screen.

Please review my file structure/layout code and provide the exact updated code blocks I need to drop into my components and a prompt i can feed into codex/replit to make the changes to the repo ensuring it remains functional, generate the prompt in a md file i can download
