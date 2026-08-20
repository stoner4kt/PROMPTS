# I'm getting a 200 code but my response is this and I

I'm getting a 200 code but my response is this and I have verified my domain in resend which is inyathitours.comi will share my exact function below the response {
  "event_message": "[fault-alert] Resend API Response: {\n  status: 403,\n  ok: false,\n  data: {\n    statusCode: 403,\n    name: \"validation_error\",\n    message: \"You can only send testing emails to your own email address (brentberthly@gmail.com). To send emails to other recipients, please verify a domain at resend.com/domains, and change the `from` address to an email using this domain.\"\n  }\n}\n",
  "id": "2fc31138-fe82-4c75-b5ab-c52af0779b48",
  "metadata": [
    {
      "boot_time": null,
      "cpu_time_used": null,
      "deployment_id": "jxsesdcwdjrxydkvhpsh_9b61ae34-674a-40fb-8fcd-bc0d44a01a70_45",
      "event_type": "Log",
      "execution_id": "d425328f-1cfa-4358-9678-211be43ab549",
      "function_id": "9b61ae34-674a-40fb-8fcd-bc0d44a01a70",
      "level": "info",
      "memory_used": [],
      "project_ref": "jxsesdcwdjrxydkvhpsh",
      "reason": null,
      "region": "eu-west-3",
      "served_by": "supabase-edge-runtime-1.74.2 (compatible with Deno v2.1.4)",
      "timestamp": "2026-07-01T20:25:12.960Z",
      "version": "45"
    }
  ],
  "timestamp": 1782937512960000
}.    ( import { serve } from 'https://deno.land/std@0.177.0/http/server.ts';
import { createClient } from 'https://esm.sh/@supabase/supabase-js@2';

const corsHeaders = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers': '*',
  'Access-Control-Allow-Methods': 'POST, OPTIONS',
};

serve(async (req: Request) => {
  if (req.method === 'OPTIONS') return new Response('ok', { headers: corsHeaders });
  if (req.method !== 'POST') {
    return new Response(JSON.stringify({ error: 'Method not allowed' }), {
      status: 405, headers: { ...corsHeaders, 'Content-Type': 'application/json' }
    });
  }

  try {
    const body = await req.json();
    console.log('[fault-alert] Payload received:', JSON.stringify(body));

    const { vehicle_reg, driver_id, faults, inspection_id, invoice_no, notes } = body;

    if (!vehicle_reg || !Array.isArray(faults) || faults.length === 0) {
      return new Response(JSON.stringify({ error: 'Missing required fields' }), { status: 400, headers: { ...corsHeaders, 'Content-Type': 'application/json' } });
    }

    const resendApiKey = Deno.env.get('RESEND_API_KEY') ?? '';
    if (!resendApiKey) {
      console.error('[fault-alert] RESEND_API_KEY missing');
      return new Response(JSON.stringify({ error: 'Resend API key not configured' }), { status: 500, headers: { ...corsHeaders, 'Content-Type': 'application/json' } });
    }

    const adminEmailRaw = Deno.env.get('ADMIN_EMAIL') ?? '';
    const toEmails = adminEmailRaw.split(',').map(e => e.trim()).filter(Boolean);
    if (toEmails.length === 0) toEmails.push('reeqieric41@gmail.com');

    console.log('[fault-alert] Sending to emails:', toEmails);

    const fromEmail = Deno.env.get('SENDER_EMAIL') ?? 'Inyathi Alerts <onboarding@resend.dev>';

    const timestamp = new Date().toLocaleString('en-ZA', { timeZone: 'Africa/Johannesburg' });

    const faultListText = faults.map((f: string, i: number) => `${i+1}. ${f}`).join('\n');

    const rawText = `🚨 CRITICAL FAULT ALERT — INYATHI 🚨\n\nVehicle: ${vehicle_reg}\nDriver: ${driver_id ?? 'N/A'}\nTime: ${timestamp}\nBooking: ${invoice_no ?? 'N/A'}\n\nFaults:\n${faultListText}\n\n${notes ? `Notes: ${notes}\n\n` : ''}Action required: Inspect vehicle before next trip.`;

    console.log('[fault-alert] Calling Resend API...');

    const resendResponse = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${resendApiKey}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        from: fromEmail,
        to: toEmails,
        subject: `🚨 CRITICAL FAULT: ${vehicle_reg}`,
        text: rawText,
      }),
    });

    const responseData = await resendResponse.json();

    console.log('[fault-alert] Resend Response:', {
      status: resendResponse.status,
      ok: resendResponse.ok,
      body: responseData
    });

    const success = resendResponse.ok;

    if (success && inspection_id) {
      try {
        const adminClient = createClient(
          Deno.env.get('SUPABASE_URL') ?? '',
          Deno.env.get('SUPABASE_SERVICE_ROLE_KEY') ?? '',
        );
        await adminClient.from('inspections').update({ alert_sent: true }).eq('id', inspection_id);
        console.log('[fault-alert] Updated inspection alert_sent = true');
      } catch (e) {
        console.error('[fault-alert] DB update error:', e);
      }
    }

    return new Response(JSON.stringify({ success, resend: responseData }), {
      headers: { ...corsHeaders, 'Content-Type': 'application/json' },
    });

  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    console.error('[fault-alert] Critical error:', message);
    return new Response(JSON.stringify({ error: message }), {
      status: 500,
      headers: { ...corsHeaders, 'Content-Type': 'application/json' },
    });
  }
});

---

So what if I don't have a dedicated email for this as the ADMIN_EMAIL is also a email on this domain so should I just use another that's already created on this domain and insert it because I already verified the domain in resend

---

Okay this is the responses : {
  "event_message": "[fault-alert] Resend API Response: {\n  status: 200,\n  ok: true,\n  data: { id: \"9de8cd47-46d5-4c68-a7b8-bcfff6b65004\" }\n}\n",
  "id": "66277e8b-738d-4cd3-8b43-eb918fbb4a87",
  "metadata": [
    {
      "boot_time": null,
      "cpu_time_used": null,
      "deployment_id": "jxsesdcwdjrxydkvhpsh_9b61ae34-674a-40fb-8fcd-bc0d44a01a70_46",
      "event_type": "Log",
      "execution_id": "015b8d5c-0cdd-4481-8910-aa7a1fc22601",
      "function_id": "9b61ae34-674a-40fb-8fcd-bc0d44a01a70",
      "level": "info",
      "memory_used": [],
      "project_ref": "jxsesdcwdjrxydkvhpsh",
      "reason": null,
      "region": "eu-west-3",
      "served_by": "supabase-edge-runtime-1.74.2 (compatible with Deno v2.1.4)",
      "timestamp": "2026-07-01T20:43:11.421Z",
      "version": "46"
    }
  ],
  "timestamp": 1782938591421000
}   And this: {
  "event_message": "[fault-alert] Updated inspection alert_sent flag\n",
  "id": "dca24fce-2c26-4f10-9d18-0485ce60d33e",
  "metadata": [
    {
      "boot_time": null,
      "cpu_time_used": null,
      "deployment_id": "jxsesdcwdjrxydkvhpsh_9b61ae34-674a-40fb-8fcd-bc0d44a01a70_46",
      "event_type": "Log",
      "execution_id": "015b8d5c-0cdd-4481-8910-aa7a1fc22601",
      "function_id": "9b61ae34-674a-40fb-8fcd-bc0d44a01a70",
      "level": "info",
      "memory_used": [],
      "project_ref": "jxsesdcwdjrxydkvhpsh",
      "reason": null,
      "region": "eu-west-3",
      "served_by": "supabase-edge-runtime-1.74.2 (compatible with Deno v2.1.4)",
      "timestamp": "2026-07-01T20:43:11.602Z",
      "version": "46"
    }
  ],
  "timestamp": 1782938591602000
}.  Is it working
