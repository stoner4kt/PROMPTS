# Role: Senior Full-Stack Developer Task: Upgrade my existing Netlify Function to handle

Role: Senior Full-Stack Developer

Task: Upgrade my existing Netlify Function to handle a dual-purpose E-commerce backend.

Function Logic Requirements:

Route A (Admin - Product Upload): Accept product details (name, price, stock) and a Base64 image. Upload the image to Cloudinary, then save the resulting URL and product details into a Firestore collection named products.

Route B (User - Checkout): Accept order details and a Base64 string of the payment proof. Upload the proof to Cloudinary (into a folder named 'payments'), save the order to Firestore (orders), and append the order details (including the image link) to a Google Sheet.

Technical Requirements:

Use firebase-admin for database operations.

Use cloudinary (v2) for image hosting.

Use google-spreadsheet and google-auth-library for the spreadsheet sync.

Error Handling: Wrap each service (Cloudinary, Sheets, Firebase) in a try-catch block. If the Spreadsheet fails, the function should still return a success if Firebase succeeded, but include a warning in the logs.

Environment Variables: Correctly parse \n for all private keys.

Headers: If the Google Sheet is empty, automatically create headers: Order_ID, Customer_Name, Total_Amount, Payment_Proof_URL, Timestamp.

---

Provide me a step by step guide to setting this up
