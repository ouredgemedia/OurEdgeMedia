/**
 * ====================================================================
 * OUR EDGE MEDIA - GOOGLE APPS SCRIPT FOR GOOGLE SHEETS
 * ====================================================================
 * 
 * Target Spreadsheet:
 * https://docs.google.com/spreadsheets/d/1j11WN6BBb75lK5c1h86FZ-3X_loliBpskUBaMtPBAd4/edit?usp=sharing
 * 
 * --------------------------------------------------------------------
 * SETUP INSTRUCTIONS (हिंदी में निर्देश):
 * --------------------------------------------------------------------
 * 1. Apni Google Sheet open karein:
 *    https://docs.google.com/spreadsheets/d/1j11WN6BBb75lK5c1h86FZ-3X_loliBpskUBaMtPBAd4/edit
 * 
 * 2. Top menu mein "Extensions" (एक्सटेंशन) par click karein aur "Apps Script" chunein.
 * 
 * 3. Jo default code dikhe use delete karein aur yeh poora code waha paste kar dein.
 * 
 * 4. Save icon (floppy disk) par click karein.
 * 
 * 5. Top-right mein blue color ke "Deploy" button par click karein -> "New deployment" select karein.
 * 
 * 6. "Select type" gear icon par click karke "Web app" select karein:
 *    - Description: Our Edge Media Form Submissions
 *    - Execute as: "Me" (Aapki Gmail id)
 *    - Who has access: "Anyone" (Bina login kiye har koi form submit kar sake)
 * 
 *    IMPORTANT: Code badalne ke baad hamesha "Deploy" -> "Manage deployments" ->
 *    pencil (Edit) icon -> Version: "New version" -> "Deploy" karein.
 *    Warna purana code hi chalta rahega (error: "Script function not found").
 *
 * 7. "Deploy" button par click karein (Google authorization permission maange toh Allow karein).
 * 
 * 8. Aapko ek "Web app URL" milega (https://script.google.com/macros/s/.../exec).
 *    Uss URL ko copy karke apne project ki `sheet-api.js` file mein
 *    `GOOGLE_SHEET_SCRIPT_URL` ki jagah paste kar dein.
 * 
 * Done! Ab har registration form, send message aur chat enquiry automatic sheet mein alag-alag tabs mein save hogi!
 * ====================================================================
 */

function doPost(e) {
  // Lock so simultaneous submissions never overwrite each other
  var lock = LockService.getScriptLock();
  lock.waitLock(20000);
  try {
    var sheetId = "1j11WN6BBb75lK5c1h86FZ-3X_loliBpskUBaMtPBAd4";
    var ss = SpreadsheetApp.openById(sheetId);

    var data = {};
    if (e.postData && e.postData.contents) {
      try {
        data = JSON.parse(e.postData.contents);
      } catch (err) {
        data = e.parameter || {};
      }
    } else if (e.parameter) {
      data = e.parameter;
    }

    var formType = (data.formType || data.type || "General").toString().toLowerCase();
    var timestamp = data.timestamp || Utilities.formatDate(new Date(), "Asia/Kolkata", "dd/MM/yyyy HH:mm:ss");

    if (formType.indexOf("registration") !== -1) {
      // 1. REGISTRATION APPLICATION TAB
      var sheet = getOrCreateTab(ss, "Registrations", [
        "Timestamp", "Name", "Mobile Number", "Location", "Brand Name", "Work Type"
      ]);
      sheet.appendRow([
        timestamp,
        clean(data.name),
        clean(data.mobile || data.phone),
        clean(data.location),
        clean(data.brand),
        clean(data.workType || data.work)
      ]);

    } else if (formType.indexOf("contact") !== -1 || formType.indexOf("message") !== -1) {
      // 2. CONTACT US (SEND MESSAGE) TAB
      var sheet = getOrCreateTab(ss, "Contact Messages", [
        "Timestamp", "Name", "Email", "Subject", "Message", "Phone", "Page"
      ]);
      sheet.appendRow([
        timestamp,
        clean(data.name),
        clean(data.email),
        clean(data.subject),
        clean(data.message),
        clean(data.phone),
        clean(data.page)
      ]);

    } else if (formType.indexOf("chat") !== -1) {
      // 3. AI CHATBOT INQUIRIES TAB
      var sheet = getOrCreateTab(ss, "Chat Inquiries", [
        "Timestamp", "User Query", "AI Reply"
      ]);
      sheet.appendRow([
        timestamp,
        clean(data.query || data.message),
        clean(data.reply)
      ]);

    } else {
      // 4. FALLBACK / GENERAL TAB
      var sheet = getOrCreateTab(ss, "All Submissions", [
        "Timestamp", "Type", "Name", "Contact", "Subject / Location", "Details"
      ]);
      sheet.appendRow([
        timestamp,
        data.formType || "General",
        data.name || "",
        data.mobile || data.email || "",
        data.subject || data.location || "",
        data.message || data.brand || JSON.stringify(data)
      ]);
    }

    return ContentService.createTextOutput(JSON.stringify({ status: "success", message: "Data saved successfully" }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (error) {
    return ContentService.createTextOutput(JSON.stringify({ status: "error", error: error.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  } finally {
    lock.releaseLock();
  }
}

// Helper: trims input and blocks spreadsheet formula injection (=, +, -, @)
function clean(value) {
  var v = (value === undefined || value === null) ? "" : String(value).trim();
  if (/^[=+\-@]/.test(v)) v = "'" + v;
  return v;
}

function doGet(e) {
  return ContentService.createTextOutput(JSON.stringify({
    status: "active",
    message: "Our Edge Media Google Sheet API is live and working!"
  })).setMimeType(ContentService.MimeType.JSON);
}

// Helper: Tab dhunde ya automatically branded header row ke sath create kare
function getOrCreateTab(ss, tabName, headers) {
  var sheet = ss.getSheetByName(tabName);
  if (!sheet) {
    sheet = ss.insertSheet(tabName);
    sheet.appendRow(headers);

    // Style the header row in Our Edge Media Gold & Black
    var headerRange = sheet.getRange(1, 1, 1, headers.length);
    headerRange.setBackground("#FFD400");
    headerRange.setFontColor("#111111");
    headerRange.setFontWeight("bold");
    headerRange.setFontSize(11);
    headerRange.setHorizontalAlignment("center");
    sheet.setFrozenRows(1);

    // Auto-fit column widths
    for (var i = 1; i <= headers.length; i++) {
      sheet.setColumnWidth(i, 180);
    }
  } else if (sheet.getLastColumn() < headers.length) {
    // Tab already exists from an older version: add any new header columns
    var start = sheet.getLastColumn() + 1;
    var extra = headers.slice(start - 1);
    var range = sheet.getRange(1, start, 1, extra.length);
    range.setValues([extra]);
    range.setBackground("#FFD400").setFontColor("#111111").setFontWeight("bold").setHorizontalAlignment("center");
  }
  return sheet;
}

