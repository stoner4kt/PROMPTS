# https://github

https://github.com/stoner4kt/ToursystemV2refactored/tree/main    analyze my repo and and want to ensure that when admin request to edit a booking it uses the send-otp-email and verify-otp in supabase/functions/**  and supabase/schema/schema-latest.sql as the admin should be able to request a edit on bookings and drivers should be able to request edits on transfer recon sheets which sends a otp to the main admin ,it was using mock information, tell me exactly what to change and where to fix the system . I deployed the function and made the edits but the function response is a 500 error saying: {
  "event_message": "send-otp-email error: DB insert failed: invalid input syntax for type uuid: \"INV-2026-865\"\n",
  "id": "728cee9d-2261-4a02-8655-d7639bfdb72d",
  "metadata": [
    {
      "boot_time": null,
      "cpu_time_used": null,
      "deployment_id": "jxsesdcwdjrxydkvhpsh_beca9b51-4f39-4a9a-9a5a-b290a5338342_26",
      "event_type": "Log",
      "execution_id": "0d670417-19a3-44ee-946f-1d23c9bb8795",
      "function_id": "beca9b51-4f39-4a9a-9a5a-b290a5338342",
      "level": "error",
      "memory_used": [],
      "project_ref": "jxsesdcwdjrxydkvhpsh",
      "reason": null,
      "region": "eu-west-3",
      "served_by": "supabase-edge-runtime-1.74.2 (compatible with Deno v2.1.4)",
      "timestamp": "2026-07-02T13:39:03.455Z",
      "version": "26"
    }
  ],
  "timestamp": 1782999543455000
}

---

So it was working in my previous system as is , because edits and deletion requests logs who made what to booking_edit_log , booking_delete_requests

---

Okay tell me exactly what to change and where to so that the system works
