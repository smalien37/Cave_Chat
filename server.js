const express = require('express');
const bodyParser = require('body-parser');
const nodemailer = require('nodemailer');

const app = express();
const port = 3000;

app.use(express.static('public'));
app.use(bodyParser.urlencoded({ extended: true }));

app.post('/process_form', (req, res) => {
    const { name, email } = req.body;

    // Configure nodemailer to send an email
    const transporter = nodemailer.createTransport({
        service: 'gmail',
        auth: {
            user: 'nikstesla2@gmail.com',
            pass: 'jstz asob cest xmyy'
        }
    });

    const mailOptions = {
        from: 'nikstesla2@gmail.com',
        to: 'nikstesla2@gmail.com',
        subject: 'New Form Submission',
        text: `Name: ${name}\nEmail: ${email}`
    };

    transporter.sendMail(mailOptions, (error, info) => {
        if (error) {
            console.error(error);
            res.status(500).send('Internal Server Error');
        } else {
            console.log('Email sent: ' + info.response);
            res.send('Form submitted successfully!');
        }
    });
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
