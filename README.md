# Major Auto Insurance Customer Information Form

A Flask-based web application that allows customers to submit their information and required documents for insurance services. The form collects personal details, contact information, and document uploads, then automatically sends the data via email to the insurance company.

## Main Use Case
This site was essential in enabling the sales team at Major Auto Insurance to automate the process of receiving basic information and document uploads from customers. Using this application, the business was able to handle a much higher volume of sales than they would meeting with clients individually. It was mainly used during a period when many teachers from foreign countries were coming to the states to teach immersion programs and needed insurance.

## Features

- **Customer Information Collection**: Comprehensive form for personal and contact details
- **Document Upload**: Support for multiple file types (images and PDFs)
- **Input Validation**: Validation for names, addresses, phone numbers, and email addresses
- **Email Integration**: Automatic email sending with attachments
- **Responsive Design**: Bootstrap-based UI that works on all devices
- **Error Handling**: User-friendly error messages and form persistence

## Tech Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, Bootstrap, JavaScript
- **Email**: SMTP with MIME support
- **Validation**: Custom validators with phonenumbers and email-validator libraries
- **Configuration**: ConfigParser for secure credential management

## Security

- All form data is validated server-side
- File uploads are restricted to specific MIME types
- Email credentials are stored securely in configuration files

## License

This project is open-source and available under the [MIT License](https://opensource.org/license/mit).

---

**Note**: This application is designed for the specific needs of Major Auto Insurance. If you want to use this as a template for your own website, feel free to customize the branding, form fields, and email templates as needed for your use case.