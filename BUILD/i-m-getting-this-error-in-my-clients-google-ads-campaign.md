# I'm getting this error in my clients Google ads campaign

I'm getting this error in my clients Google ads campaign

---

So my clients website is at https://github.com/stoner4kt/Appliance-911-LIVE.git in my github analyze it and get back to me with the fixes I need to apply to solve this

---

So it's on my phone call from the website lead conversion and I also have these errors popping up

---

Guide me step by step how to fix this

---

So it my phone call on my website and it says this Enhanced conversions diagnostics alerts

Status,Alert title,Alert description
Needs attention,"Implement in-page code in addition to Automatic for better results","Based on your current coverage, you might get more accurate conversion data if you edit your website code."

---

Generate me a prompt i can feed into cluade to analyze the repo and outut a prompt i can feed into codex/replit to apply the fixes, or you create a new branch, apply the fixes and push it to the new branch

---

Apply the changes to the repo stoner4kt/Appliance-911-LIVE on a new branch named Ad fix

---

I see in the prompt you are mistaking my form submissions label for my phone call lead label

---

Could it be because they are together that it's failing

---

Here's is my tracking.js /* Appliance-911 — Conversion Tracking
   Google Ads ID: AW-18049545656
   Conversion types: Form Submit, Phone Click, WhatsApp Click
*/

(function () {
  var FORM_CONVERSION_SEND_TO = 'AW-18049545656/1agYCKP-msIcELjr2J5D';
  var PHONE_CONVERSION_SEND_TO = 'AW-18049545656/nPl-CL6wtsIcELjr2J5D';
  // Add the Google Ads WhatsApp conversion label here when one is available.
  var WHATSAPP_CONVERSION_SEND_TO = '';

  function fireConversion(sendTo) {
    if (!sendTo || typeof gtag !== 'function') {
      return;
    }

    gtag('event', 'conversion', {
      'send_to': sendTo
    });
  }

  // ── 1. FORM SUBMISSION CONVERSIONS ─────────────────────────────────────
  // Fires when any Netlify/standard form is submitted
  document.addEventListener('DOMContentLoaded', function () {

    var forms = document.querySelectorAll('form[name="repair-booking"], form[data-netlify="true"]');

    forms.forEach(function (form) {
      form.addEventListener('submit', function () {
        fireConversion(FORM_CONVERSION_SEND_TO);
      });
    });

    // ── 2. PHONE CLICK CONVERSIONS ────────────────────────────────────────
    // Fires on any tel: link click anywhere on the page
    document.addEventListener('click', function (e) {
      var target = e.target.closest('a[href^="tel:"]');
      if (target) {
        fireConversion(PHONE_CONVERSION_SEND_TO);
      }
    });

    // ── 3. WHATSAPP CLICK CONVERSIONS ─────────────────────────────────────
    // Fires on any wa.me link or the floating WhatsApp button once a label is configured
    document.addEventListener('click', function (e) {
      var target = e.target.closest('a[href*="wa.me"], a[href*="api.whatsapp.com"], .whatsapp-float');
      if (target) {
        fireConversion(WHATSAPP_CONVERSION_SEND_TO);
      }
    });

  });

})();

---

So why was it working saying active when I first deploy it

---

Okay now how do i setup the WhatsApp one and get it's label

---

Should I just choose manually with code because their us only automatically without code,

---

I just updated the empty space in the previous code u gave me and uploaded it 

Okay I added it to my tag, now I want to make sure the all the Call  buttons and WhatsApp floating icons and booking form button are tracked across all pages with it present. Generate me a prompt i can feed into cluade to analyze the repo and output a prompt i can then feed into replit to perform the task

---

So didn't run the prompts but I uploaded the tracking.js but it still says needs  attention

---

Yes as the need attention is limiting my campaign, can I just remove that conversion and add a new one

---

Okay I removed the old one and added a new one and also added it's label to tracking.js but the need attention is still showing on my campaign
