const express = require('express');
const nodemailer = require('nodemailer');
const cors = require('cors');
const app = express();
const PORT = 3001;

app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.post('/contact', async (req, res) => {
  const { name, email, mobile, message } = req.body;

  // Configure your SMTP transport (update with your real credentials)
  const transporter = nodemailer.createTransport({
    host: 'smtp.gmail.com',
    port: 465,
    secure: true,
    auth: {
      user: 'your-email@gmail.com', // Replace with your email
      pass: 'your-app-password'     // Replace with your app password
    }
  });

  const mailOptions = {
    from: email,
    to: 'contact@eyeonfleet.com',
    subject: 'New Contact Form Submission',
    text: `Name: ${name}\nEmail: ${email}\nMobile: ${mobile}\nMessage: ${message}`
  };

  try {
    await transporter.sendMail(mailOptions);
    res.status(200).json({ success: true, message: 'Email sent successfully!' });
  } catch (error) {
    res.status(500).json({ success: false, message: 'Failed to send email.', error });
  }
});

app.listen(PORT, () => {
  console.log(`Contact form backend running on http://localhost:${PORT}`);
});
