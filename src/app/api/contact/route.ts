import { NextResponse } from "next/server";

export async function POST(req: Request) {
  try {
    const body = await req.json();
    const { name, email, subject, message } = body;

    // Server-side validations
    if (!name || typeof name !== "string" || name.trim().length < 2) {
      return NextResponse.json(
        { success: false, message: "Please provide a valid name (at least 2 characters)." },
        { status: 400 }
      );
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!email || !emailRegex.test(email)) {
      return NextResponse.json(
        { success: false, message: "Please provide a valid email address." },
        { status: 400 }
      );
    }

    if (!subject || typeof subject !== "string" || subject.trim().length < 3) {
      return NextResponse.json(
        { success: false, message: "Please provide a subject line." },
        { status: 400 }
      );
    }

    if (!message || typeof message !== "string" || message.trim().length < 10) {
      return NextResponse.json(
        { success: false, message: "Message must be at least 10 characters long." },
        { status: 400 }
      );
    }

    // Optional SendGrid delivery if configured in environment
    const sendgridApiKey = process.env.SENDGRID_API_KEY;
    const recipientEmail = process.env.CONTACT_RECIPIENT_EMAIL;

    if (sendgridApiKey && recipientEmail) {
      try {
        const response = await fetch("https://api.sendgrid.com/v3/mail/send", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${sendgridApiKey}`,
          },
          body: JSON.stringify({
            personalizations: [{ to: [{ email: recipientEmail }] }],
            from: { email: recipientEmail, name: `Portfolio Contact: ${name}` },
            reply_to: { email, name },
            subject: `[Portfolio Contact] ${subject}`,
            content: [
              {
                type: "text/plain",
                value: `Name: ${name}\nEmail: ${email}\n\nMessage:\n${message}`,
              },
            ],
          }),
        });

        if (!response.ok) {
          console.error("SendGrid API error:", await response.text());
        }
      } catch (sgError) {
        console.error("Failed to forward email via SendGrid:", sgError);
      }
    }

    return NextResponse.json(
      {
        success: true,
        message: "Thank you for reaching out! Your message has been received.",
      },
      { status: 200 }
    );
  } catch (error) {
    console.error("Contact API internal error:", error);
    return NextResponse.json(
      { success: false, message: "Internal server error. Please try again later." },
      { status: 500 }
    );
  }
}
