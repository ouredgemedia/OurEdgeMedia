/**
 * Our Edge Media - Google Sheet Integration API
 *
 * Google Spreadsheet:
 * https://docs.google.com/spreadsheets/d/1j11WN6BBb75lK5c1h86FZ-3X_loliBpskUBaMtPBAd4/edit?usp=sharing
 *
 * Instructions:
 * 1. Open your Google Sheet
 * 2. Click Extensions > Apps Script
 * 3. Paste the code from GoogleAppsScript.gs and Deploy as Web App
 * 4. Paste the Web App URL below into GOOGLE_SHEET_SCRIPT_URL:
 */

const GOOGLE_SHEET_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbwl8pNRiU_ShVaWieAm5ozMu7wssPswOCc6U3E20DsNkCUiBK_rH45hwM41WI7TFg0/exec";

const OEM_WHATSAPP_URL = "https://wa.me/919196497565";

/**
 * Sends form & chat data to Google Sheet and waits for the script's real reply.
 * @param {Object} data
 * @returns {Promise<boolean>} true only when the sheet confirms the row was saved
 */
async function sendToGoogleSheet(data) {
    if (!data.timestamp) {
        data.timestamp = new Date().toLocaleString("en-IN", { timeZone: "Asia/Kolkata" });
    }

    if (!GOOGLE_SHEET_SCRIPT_URL || GOOGLE_SHEET_SCRIPT_URL.includes("YOUR_DEPLOYED_SCRIPT_ID")) {
        console.error("[Google Sheets] Web App URL not configured in sheet-api.js.");
        return false;
    }

    try {
        // text/plain keeps this a "simple" request (no CORS preflight), and Apps Script
        // replies with Access-Control-Allow-Origin: *, so we can read the JSON result.
        const res = await fetch(GOOGLE_SHEET_SCRIPT_URL, {
            method: "POST",
            redirect: "follow",
            headers: { "Content-Type": "text/plain;charset=utf-8" },
            body: JSON.stringify(data)
        });
        const text = await res.text();
        let json = null;
        try { json = JSON.parse(text); } catch (e) { /* Google returned an HTML error page */ }

        if (json && json.status === "success") return true;

        if (!json && /Script function not found/i.test(text)) {
            console.error("[Google Sheets] Deployed script has no doPost(). Paste GoogleAppsScript.gs into Apps Script and deploy a NEW VERSION.");
        } else {
            console.error("[Google Sheets] Save failed:", json ? json.error : text.slice(0, 300));
        }
        return false;
    } catch (err) {
        console.error("[Google Sheets] Network error saving data:", err);
        return false;
    }
}

/**
 * Branded popup used instead of the browser's plain alert().
 * @param {"success"|"error"} type
 * @param {string} title
 * @param {string} message
 */
function showFormPopup(type, title, message) {
    if (!document.getElementById("oem-popup-style")) {
        const style = document.createElement("style");
        style.id = "oem-popup-style";
        style.textContent = `
            .oem-popup-overlay { position: fixed; inset: 0; background: rgba(0, 0, 0, .55); backdrop-filter: blur(4px);
                -webkit-backdrop-filter: blur(4px); display: flex; align-items: center; justify-content: center;
                padding: 16px; z-index: 2147483000; opacity: 0; transition: opacity .2s ease; }
            .oem-popup-overlay.show { opacity: 1; }
            .oem-popup { width: min(100%, 420px); background: #fff; border: 1px solid #E7E7E7;
                border-radius: 20px; padding: 32px 26px 26px; text-align: center; color: #1F1F1F;
                font-family: 'Source Sans 3', system-ui, sans-serif; box-shadow: 0 24px 48px -12px rgba(0, 0, 0, .3);
                transform: translateY(14px) scale(.97); transition: transform .25s cubic-bezier(.2,.7,.2,1); }
            .oem-popup-overlay.show .oem-popup { transform: none; }
            .oem-popup-icon { width: 64px; height: 64px; margin: 0 auto 18px; border-radius: 50%; display: flex;
                align-items: center; justify-content: center; font-size: 28px; }
            .oem-popup.success .oem-popup-icon { background: #FFCC00; color: #000000; }
            .oem-popup.error .oem-popup-icon { background: #000000; color: #FFCC00; }
            .oem-popup h3 { font-family: 'Lexend', system-ui, sans-serif; font-size: 22px; font-weight: 600; margin: 0 0 8px; color: #0A0A0A; }
            .oem-popup p { font-size: 16px; line-height: 1.6; color: #525252; margin: 0 0 22px; }
            .oem-popup-actions { display: flex; flex-direction: column; gap: 10px; }
            .oem-popup-btn { min-height: 48px; border-radius: 10px; border: none; font-weight: 600; font-size: 16px;
                font-family: 'Lexend', system-ui, sans-serif; cursor: pointer; display: inline-flex; align-items: center; justify-content: center;
                gap: 8px; text-decoration: none; transition: background .2s ease; }
            .oem-popup-btn.primary { background: #FFCC00; color: #000000; }
            .oem-popup-btn.primary:hover { background: #FFD633; }
            .oem-popup-btn.wa { background: #000000; color: #fff; } .oem-popup-btn.wa i { color: #FFCC00; }
            .oem-popup-btn.wa:hover { background: #000000; }
            .oem-popup-btn:focus-visible { outline: 3px solid rgba(255, 204, 0, .4); outline-offset: 2px; }
        `;
        document.head.appendChild(style);
    }

    const old = document.querySelector(".oem-popup-overlay");
    if (old) old.remove();

    const overlay = document.createElement("div");
    overlay.className = "oem-popup-overlay";
    overlay.innerHTML = `
        <div class="oem-popup ${type}" role="alertdialog" aria-modal="true" aria-labelledby="oemPopupTitle">
            <div class="oem-popup-icon"><i class="fas ${type === "success" ? "fa-check" : "fa-triangle-exclamation"}"></i></div>
            <h3 id="oemPopupTitle"></h3>
            <p></p>
            <div class="oem-popup-actions">
                ${type === "error" ? `<a class="oem-popup-btn wa" href="${OEM_WHATSAPP_URL}" target="_blank" rel="noopener noreferrer"><i class="fab fa-whatsapp"></i> Chat on WhatsApp</a>` : ""}
                <button type="button" class="oem-popup-btn primary">${type === "success" ? "Done" : "Close"}</button>
            </div>
        </div>`;
    overlay.querySelector("h3").textContent = title;
    overlay.querySelector("p").textContent = message;

    const close = () => {
        overlay.classList.remove("show");
        document.removeEventListener("keydown", onKey);
        setTimeout(() => overlay.remove(), 250);
    };
    const onKey = (e) => { if (e.key === "Escape") close(); };
    overlay.querySelector("button").addEventListener("click", close);
    overlay.addEventListener("click", (e) => { if (e.target === overlay) close(); });
    document.addEventListener("keydown", onKey);

    document.body.appendChild(overlay);
    requestAnimationFrame(() => overlay.classList.add("show"));
    overlay.querySelector("button").focus();
}
