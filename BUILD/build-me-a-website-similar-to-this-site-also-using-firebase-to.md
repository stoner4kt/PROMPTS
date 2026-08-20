# Build me a website similar to this site also using firebase to

Build me a website similar to this site also using firebase to store data. Add a admin panel where the admin can upload new products with images, prices and names, update stock levels and view orders made. Use the same order form only add in that the customer should upload a images showing proof of payment before placing order. Remove the game logic and prize system. The business name is Herbal Hights. And use color themes of yellow and green. Optimize the design for all screens and devices especially mobile.

---

Context: I am using a Netlify Function as my backend bridge to save data to both Firestore and Google Sheets. I am hosting on Netlify and using the Firebase JS SDK for other parts of my app.

Task: Please modify my existing Netlify Function (attached below) to include the following:

Firebase Admin Integration: Initialize firebase-admin using environment variables for the service account (PROJECT_ID, CLIENT_EMAIL, PRIVATE_KEY).

Google Sheets Integration: Use the google-spreadsheet and google-auth-library packages to append the incoming request data as a new row in a specific Google Sheet.

Error Handling: Ensure that if one service fails (e.g., Google Sheets is down), the function provides a clear error but still attempts to complete the other operation if possible.

Formatting: Correctly handle the \n characters in the private keys so they work in the Netlify environment.

Constraints:

Do not remove any of my existing validation logic or other helper functions.

Use async/await syntax.

Provide the updated package.json dependencies I need to install.   Additional Instruction: > "If the Google Sheet is empty, the function should first check for a header row. If no headers exist, use setHeaderRow() to automatically create headers based on the keys of the incoming JSON object before appending the data.

---

I don't have no netlify functions file
