from django.shortcuts import render
from django.utils.safestring import mark_safe

navbar = {'login': 'Login', 'ceos': 'CEOs', 'buyer': 'Buyer', 'seller': 'Seller', 'government': 'Government', 'agent': 'Agent'}
footer = {}
cookie_policy = {'cookie_policy_text': 'This site uses cookies. When you click on ACCEPT or if you continue browsing cookies might be installed on your device', 'cookie_policy_link': 'Privacy Policy', 'cookie_policy_button_text': 'Accept'}

def index(request):
    return render(request, 'public/index.html', {
        'page_title': 'NORTATEM | Welcome',
        'page_css': 'public/css/index.css', #optional
        'page_js': 'public/js/index.js', #optional
        'page_keywords': 'NORTATEM, B2B marketplace, chatGPT, language model, machine learning, wholesalers, distributors, sellers, purchasing managers, sales, B2B sales, find B2B buyers, find B2B suppliers, machine learning, automated sales, artificial intelligence',
        'page_description': 'Looking to increase margins via sales or purchasing? With more than 7,000,000 companies from all over the world we automatize the tedious parts of selling and buying. Works from day 1. No training required',
        'navbar': navbar,
        'footer': footer,
        'cookie_policy': cookie_policy,
    })

def ceos(request):
    return render(request, 'public/ceos.html', {
        'page_title': 'NORTATEM | CEOs',
        'page_css': 'public/css/ceos.css', #optional
        # 'page_js': 'public/js/ceos.js', #optional
        'page_keywords': 'NORTATEM, CEOs, chatGPT, B2B marketplace, language model, machine learning, wholesalers, distributors, sellers, purchasing managers, sales, B2B sales, find B2B buyers, find B2B suppliers, machine learning, automated sales, artificial intelligence',
        'page_description': 'NORTATEM CEOs explains the advantages and benefits of NORTATEM for CEOs. Using a language model, our chatGPT, we explain why CEOs will not miss critical information, will have their own personal consultant, and develop an advantage in sales and purchasing over the competition',
        'navbar': navbar,
        'footer': footer,
        'cookie_policy': cookie_policy,
        'content': {
            'section_1' : {
                'title': 'Do not miss having unprecedented access to critical information about your competitors, customers, industry and company',
                'question': 'Compare my sales from yesterday with my competitors sales',
                'button_text': 'View Answer',
                'answer': 'Competitor A and B sold 582 units and 889 units at an average price of €2.79 and €2.19 respectively. Our sales were 329 units at an average price of €2.89. Based on that, would you like me to do a projection for this week?',
            },
        },
    })

def buyer(request):
    return render(request, 'public/buyer.html', {
        'page_title': 'NORTATEM | Buyer',
        # 'page_css': 'public/css/index.css', #optional
        # 'page_js': 'public/js/index.js', #optional
        # 'page_keywords': 'NORTATEM, B2B marketplace, chatGPT, language model, machine learning, wholesalers, distributors, sellers, purchasing managers, sales, B2B sales, find B2B buyers, find B2B suppliers, machine learning, automated sales, artificial intelligence',
        # 'page_description': 'Looking to increase margins via sales or purchasing? With more than 7,000,000 companies from all over the world we automatize the tedious parts of selling and buying. Works from day 1. No training required',
        'navbar': navbar,
        'footer': footer,
        'cookie_policy': cookie_policy,
    })

def seller(request):
    return render(request, 'public/seller.html', {
        'page_title': 'NORTATEM | Seller',
        # 'page_css': 'public/css/index.css', #optional
        # 'page_js': 'public/js/index.js', #optional
        # 'page_keywords': 'NORTATEM, B2B marketplace, chatGPT, language model, machine learning, wholesalers, distributors, sellers, purchasing managers, sales, B2B sales, find B2B buyers, find B2B suppliers, machine learning, automated sales, artificial intelligence',
        # 'page_description': 'Looking to increase margins via sales or purchasing? With more than 7,000,000 companies from all over the world we automatize the tedious parts of selling and buying. Works from day 1. No training required',
        'navbar': navbar,
        'footer': footer,
        'cookie_policy': cookie_policy,
    })

def government(request):
    return render(request, 'public/government.html', {
        'page_title': 'NORTATEM | Government',
        # 'page_css': 'public/css/index.css', #optional
        # 'page_js': 'public/js/index.js', #optional
        # 'page_keywords': 'NORTATEM, B2B marketplace, chatGPT, language model, machine learning, wholesalers, distributors, sellers, purchasing managers, sales, B2B sales, find B2B buyers, find B2B suppliers, machine learning, automated sales, artificial intelligence',
        # 'page_description': 'Looking to increase margins via sales or purchasing? With more than 7,000,000 companies from all over the world we automatize the tedious parts of selling and buying. Works from day 1. No training required',
        'navbar': navbar,
        'footer': footer,
        'cookie_policy': cookie_policy,
    })

def agent(request):
    return render(request, 'public/agent.html', {
        'page_title': 'NORTATEM | Agent',
        # 'page_css': 'public/css/index.css', #optional
        # 'page_js': 'public/js/index.js', #optional
        # 'page_keywords': 'NORTATEM, B2B marketplace, chatGPT, language model, machine learning, wholesalers, distributors, sellers, purchasing managers, sales, B2B sales, find B2B buyers, find B2B suppliers, machine learning, automated sales, artificial intelligence',
        # 'page_description': 'Looking to increase margins via sales or purchasing? With more than 7,000,000 companies from all over the world we automatize the tedious parts of selling and buying. Works from day 1. No training required',
        'navbar': navbar,
        'footer': footer,
        'cookie_policy': cookie_policy,
    })

def legal(request):
    return render(request, 'public/legal.html', {
        'page_title': 'NORTATEM | Legal',
        'page_css': 'public/css/legal.css', #optional
        # 'page_js': 'public/js/index.js', #optional
        'page_keywords': 'legal, legal terms, privacy policy, cookies, cookie policy, job applicants, sales, B2B sales, find B2B buyers, find B2B suppliers, machine learning, automated sales, artificial intelligence',
        'page_description': 'NORTATEM legal information, includes legal conditions, our privacy policy, our cookie policy and how we treat the information submitted by job applicants',
        'navbar': navbar,
        'footer': footer,
        'cookie_policy': cookie_policy,
        'content': {
            'page_title': 'Legal',
            'last_updated_msg': 'This document was last updated on July 2023',
            'privacy_policy': {
                'title': 'Privacy Policy',
                'introduction': 'This privacy policy ("Policy") describes how the personally identifiable information ("Personal Information") you may provide on the nortatem.com website ("NORTATEM" or "Service") and any of its related products and services (collectively, "Services") is collected, protected and used. It also describes the choices available to you regarding our use of your Personal Information and how you can access and update this information. This Policy is a legally binding agreement between you ("User", "you" or "your") and this Website operator ("Operator", "we", "us" or "our"). By accessing and using the Website and Services, you acknowledge that you have read, understood, and agree to be bound by the terms of this Policy. This Policy does not apply to the practices of companies that we do not own or control, or to individuals that we do not employ or manage.',
                'contents': [
                    {
                    'subtitle': 'Automatic collection of information',
                    'subtext': mark_safe("When you open the Website, our servers automatically record information that your browser sends. This data may include information such as your device's IP address, browser type and version, operating system type and version, language preferences or the webpage you were visiting before you came to the Website and Services, pages of the Website and Services that you visit, the time spent on those pages, information you search for on the Website, access times and dates, and other statistics.<br />Information collected automatically is used only to identify potential cases of abuse and establish statistical information regarding the usage and traffic of the Website and Services. This statistical information is not otherwise aggregated in such a way that would identify any particular user of the system.")
                    },
                    {
                    'subtitle': 'Collection of personal information',
                    'subtext': mark_safe("You can access and use the Website and Services without telling us who you are or revealing any information by which someone could identify you as a specific, identifiable individual. If, however, you wish to use some of the features on the Website, you may be asked to provide certain Personal Information (for example, your name and e-mail address). We receive and store any information you knowingly provide to us when you create an account, publish content, or fill any online forms on the Website. When required, this information may include the following:<br />- Personal details such as name, country of residence, etc.<br />- Contact information such as email address, address, etc.<br />- Account details such as user name, unique user ID, password, etc.<br />- Geolocation data such as latitude and longitude.<br />Some of the information we collect is directly from you via the Website and Services. However, we may also collect Personal Information about you from other sources such as public databases and our joint marketing partners. You can choose not to provide us with your Personal Information, but then you may not be able to take advantage of some of the features on the Website. Users who are uncertain about what information is mandatory are welcome to contact us.")
                    },
                    {
                    'subtitle': 'Use and processing of collected information',
                    'subtext': mark_safe("In order to make the Website and Services available to you, or to meet a legal obligation, we may need to collect and use certain Personal Information. If you do not provide the information that we request, we may not be able to provide you with the requested products or services. Any of the information we collect from you may be used for the following purposes:<br />- Create and manage user accounts<br />- Send administrative information<br />- Respond to inquiries and offer support<br />- Request user feedback<br />- Improve user experience<br />- Administer prize draws and competitions<br />- Enforce terms and conditions and policies<br />- Protect from abuse and malicious users<br />- Respond to legal requests and prevent harm<br />- Run and operate the Website and Services<br />Processing your Personal Information depends on how you interact with the Website and Services, where you are located in the world and if one of the following applies: (i) you have given your consent for one or more specific purposes; this, however, does not apply, whenever the processing of Personal Information is subject to California Consumer Privacy Act or European data protection law; (ii) provision of information is necessary for the performance of an agreement with you and/or for any pre-contractual obligations thereof; (iii) processing is necessary for compliance with a legal obligation to which you are subject; (iv) processing is related to a task that is carried out in the public interest or in the exercise of official authority vested in us; (v) processing is necessary for the purposes of the legitimate interests pursued by us or by a third party.<br />Note that under some legislations we may be allowed to process information until you object to such processing (by opting out), without having to rely on consent or any other of the following legal bases below. In any case, we will be happy to clarify the specific legal basis that applies to the processing, and in particular whether the provision of Personal Information is a statutory or contractual requirement, or a requirement necessary to enter into a contract.")
                    },
                    {
                    'subtitle': 'Managing information',
                    'subtext': mark_safe("You are able to delete certain Personal Information we have about you. The Personal Information you can delete may change as the Website and Services change. When you delete Personal Information, however, we may maintain a copy of the unrevised Personal Information in our records for the duration necessary to comply with our obligations to our affiliates and partners, and for the purposes described below. If you would like to delete your Personal Information or permanently delete your account, you can do so by contacting us.")
                    },
                    {
                    'subtitle': 'Disclosure of information',
                    'subtext': mark_safe("Depending on the requested Services or as necessary to complete any transaction or provide any service you have requested, we may share your information with your consent with our trusted third parties that work with us, any other affiliates and subsidiaries we rely upon to assist in the operation of the Website and Services available to you. We do not share Personal Information with unaffiliated third parties. These service providers are not authorized to use or disclose your information except as necessary to perform services on our behalf or comply with legal requirements. We may share your Personal Information for these purposes only with third parties whose privacy policies are consistent with ours or who agree to abide by our policies with respect to Personal Information. These third parties are given Personal Information they need only in order to perform their designated functions, and we do not authorize them to use or disclose Personal Information for their own marketing or other purposes.<br />We will disclose any Personal Information we collect, use or receive if required or permitted by law, such as to comply with a subpoena, or similar legal process, and when we believe in good faith that disclosure is necessary to protect our rights, protect your safety or the safety of others, investigate fraud, or respond to a government request.")
                    },
                    {
                    'subtitle': 'Retention of information',
                    'subtext': mark_safe("We will retain and use your Personal Information for the period necessary to comply with our legal obligations, resolve disputes, and enforce our agreements unless a longer retention period is required or permitted by law. We may use any aggregated data derived from or incorporating your Personal Information after you update or delete it, but not in a manner that would identify you personally. Once the retention period expires, Personal Information shall be deleted. Therefore, the right to access, the right to erasure, the right to rectification and the right to data portability cannot be enforced after the expiration of the retention period.")
                    },
                    {
                    'subtitle': 'Transfer of information',
                    'subtext': mark_safe("Depending on your location, data transfers may involve transferring and storing your information in a country other than your own. You are entitled to learn about the legal basis of information transfers to a country outside the European Union or to any international organization governed by public international law or set up by two or more countries, such as the UN, and about the security measures taken by us to safeguard your information. If any such transfer takes place, you can find out more by checking the relevant sections of this Policy or inquire with us using the information provided in the contact section.")
                    },
                    {
                    'subtitle': 'The rights of users',
                    'subtext': mark_safe("You may exercise certain rights regarding your information processed by us. In particular, you have the right to do the following: (i) you have the right to withdraw consent where you have previously given your consent to the processing of your information; (ii) you have the right to object to the processing of your information if the processing is carried out on a legal basis other than consent; (iii) you have the right to learn if information is being processed by us, obtain disclosure regarding certain aspects of the processing and obtain a copy of the information undergoing processing; (iv) you have the right to verify the accuracy of your information and ask for it to be updated or corrected; (v) you have the right, under certain circumstances, to restrict the processing of your information, in which case, we will not process your information for any purpose other than storing it; (vi) you have the right, under certain circumstances, to obtain the erasure of your Personal Information from us; (vii) you have the right to receive your information in a structured, commonly used and machine readable format and, if technically feasible, to have it transmitted to another controller without any hindrance. This provision is applicable provided that your information is processed by automated means and that the processing is based on your consent, on a contract which you are part of or on pre-contractual obligations thereof.")
                    },
                    {
                    'subtitle': 'The right to object to processing',
                    'subtext': mark_safe("Where Personal Information is processed for the public interest, in the exercise of an official authority vested in us or for the purposes of the legitimate interests pursued by us, you may object to such processing by providing a ground related to your particular situation to justify the objection.")
                    },
                    {
                    'subtitle': 'Data protection rights under GDPR',
                    'subtext': mark_safe("If you are a resident of the European Economic Area (EEA), you have certain data protection rights and the Operator aims to take reasonable steps to allow you to correct, amend, delete, or limit the use of your Personal Information. If you wish to be informed what Personal Information we hold about you and if you want it to be removed from our systems, please contact us. In certain circumstances, you have the following data protection rights:<br />- You have the right to request access to your Personal Information that we store and have the ability to access your Personal Information.<br />- You have the right to request that we correct any Personal Information you believe is inaccurate. You also have the right to request us to complete the Personal Information you believe is incomplete.<br />- You have the right to request the erase your Personal Information under certain conditions of this Policy.<br />- You have the right to object to our processing of your Personal Information.<br />- You have the right to seek restrictions on the processing of your Personal Information. When you restrict the processing of your Personal Information, we may store it but will not process it further.<br />- You have the right to be provided with a copy of the information we have on you in a structured, machine-readable and commonly used format.<br />- You also have the right to withdraw your consent at any time where the Operator relied on your consent to process your Personal Information.<br />You have the right to complain to a Data Protection Authority about our collection and use of your Personal Information. For more information, please contact your local data protection authority in the European Economic Area (EEA).")
                    },
                    {
                    'subtitle': 'How to exercise these rights',
                    'subtext': mark_safe("Any requests to exercise your rights can be directed to the Operator through the contact details provided in this document. Please note that we may ask you to verify your identity before responding to such requests. Your request must provide sufficient information that allows us to verify that you are the person you are claiming to be or that you are the authorized representative of such person. You must include sufficient details to allow us to properly understand the request and respond to it. We cannot respond to your request or provide you with Personal Information unless we first verify your identity or authority to make such a request and confirm that the Personal Information relates to you.")
                    },
                    {
                    'subtitle': 'Privacy of children',
                    'subtext': mark_safe("We do not knowingly collect any Personal Information from children under the age of 18. If you are under the age of 18, please do not submit any Personal Information through the Website and Services. We encourage parents and legal guardians to monitor their children's Internet usage and to help enforce this Policy by instructing their children never to provide Personal Information through the Website and Services without their permission. If you have reason to believe that a child under the age of 18 has provided Personal Information to us through the Website and Services, please contact us. You must also be at least 16 years of age to consent to the processing of your Personal Information in your country (in some countries we may allow your parent or guardian to do so on your behalf).")
                    },
                    {
                    'subtitle': 'Cookies',
                    'subtext': mark_safe('The Website and Services use "cookies" to help personalize your online experience. A cookie is a text file that is placed on your hard disk by a web page server. Cookies cannot be used to run programs or deliver viruses to your computer. Cookies are uniquely assigned to you, and can only be read by a web server in the domain that issued the cookie to you.<br />We may use cookies to collect, store, and track information for statistical purposes to operate the Website and Services. You have the ability to accept or decline cookies. Most web browsers automatically accept cookies, but you can usually modify your browser setting to decline cookies if you prefer. You may learn more about cookies and how they work below.')
                    },
                    {
                    'subtitle': 'Do Not Track signals',
                    'subtext': mark_safe("Some browsers incorporate a Do Not Track feature that signals to websites you visit that you do not want to have your online activity tracked. Tracking is not the same as using or collecting information in connection with a website. For these purposes, tracking refers to collecting personally identifiable information from consumers who use or visit a website or online service as they move across different websites over time. The Website and Services do not track its visitors over time and across third party websites. However, some third party sites may keep track of your browsing activities when they serve you content, which enables them to tailor what they present to you.")
                    },
                    {
                    'subtitle': 'Email marketing',
                    'subtext': mark_safe("We offer electronic newsletters to which you may voluntarily subscribe at any time. We are committed to keeping your e-mail address confidential and will not disclose your email address to any third parties except as allowed in the information use and processing section. We will maintain the information sent via e-mail in accordance with applicable laws and regulations.<br />In compliance with the CAN-SPAM Act, all e-mails sent from us will clearly state who the e-mail is from and provide clear information on how to contact the sender. You may choose to stop receiving our newsletter or marketing emails by following the unsubscribe instructions included in these emails or by contacting us. However, you will continue to receive essential transactional emails.")
                    },
                    {
                    'subtitle': 'Links to other resources',
                    'subtext': mark_safe("The Website and Services contain links to other resources that are not owned or controlled by us. Please be aware that we are not responsible for the privacy practices of such other resources or third parties. We encourage you to be aware when you leave the Website and Services and to read the privacy statements of each and every resource that may collect Personal Information.")
                    },
                    {
                    'subtitle': 'Information security',
                    'subtext': mark_safe("We secure information you provide on computer servers in a controlled, secure environment, protected from unauthorized access, use, or disclosure. We maintain reasonable administrative, technical, and physical safeguards in an effort to protect against unauthorized access, use, modification, and disclosure of Personal Information in its control and custody. However, no data transmission over the Internet or wireless network can be guaranteed. Therefore, while we strive to protect your Personal Information, you acknowledge that (i) there are security and privacy limitations of the Internet which are beyond our control; (ii) the security, integrity, and privacy of any and all information and data exchanged between you and the Website and Services cannot be guaranteed; and (iii) any such information and data may be viewed or tampered with in transit by a third party, despite best efforts.")
                    },
                    {
                    'subtitle': 'Data breach',
                    'subtext': mark_safe("In the event we become aware that the security of the Website and Services has been compromised or users Personal Information has been disclosed to unrelated third parties as a result of external activity, including, but not limited to, security attacks or fraud, we reserve the right to take reasonably appropriate measures, including, but not limited to, investigation and reporting, as well as notification to and cooperation with law enforcement authorities. In the event of a data breach, we will make reasonable efforts to notify affected individuals if we believe that there is a reasonable risk of harm to the user as a result of the breach or if notice is otherwise required by law. When we do, we will post a notice on the Website, send you an email.")
                    },
                    {
                    'subtitle': 'Changes and amendments',
                    'subtext': mark_safe("We reserve the right to modify this Policy or its terms relating to the Website and Services from time to time in our discretion and will notify you of any material changes to the way in which we treat Personal Information. When we do, we will revise the updated date at the bottom of this page. We may also provide notice to you in other ways in our discretion, such as through contact information you have provided. Any updated version of this Policy will be effective immediately upon the posting of the revised Policy unless otherwise specified. Your continued use of the Website and Services after the effective date of the revised Policy (or such other act specified at that time) will constitute your consent to those changes. However, we will not, without your consent, use your Personal Information in a manner materially different than what was stated at the time your Personal Information was collected.")
                    },
                    {
                    'subtitle': 'Acceptance of this policy',
                    'subtext': mark_safe("You acknowledge that you have read this Policy and agree to all its terms and conditions. By accessing and using the Website and Services you agree to be bound by this Policy. If you do not agree to abide by the terms of this Policy, you are not authorized to access or use the Website and Services.")
                    },
                    ],
            },
            'cookie_policy': {
                'title': 'Cookie Policy',
                'introduction': 'This cookie policy ("Policy") describes what cookies are and how and they are being used by the nortatem.com ("NORTATEM" or "Service") and any of its related products and services (collectively, "Services"). This Policy is a legally binding agreement between you ("User", "you" or "your") and this Website operator ("Operator", "we", "us" or "our"). You should read this Policy so you can understand the types of cookies we use, the information we collect using cookies and how that information is used. It also describes the choices available to you regarding accepting or declining the use of cookies.',
                'contents': [
                    {
                    'subtitle': 'What are cookies?',
                    'subtext': mark_safe('Cookies are small pieces of data stored in text files that are saved on your computer or other devices when websites are loaded in a browser. They are widely used to remember you and your preferences, either for a single visit (through a "session cookie") or for multiple repeat visits (using a "persistent cookie").<br />Session cookies are temporary cookies that are used during the course of your visit to the Website, and they expire when you close the web browser.<br />Persistent cookies are used to remember your preferences within our Website and remain on your desktop or mobile device even after you close your browser or restart your computer. They ensure a consistent and efficient experience for you while visiting the Website and Services.<br />Cookies may be set by the Website ("first-party cookies"), or by third parties, such as those who serve content or provide advertising or analytics services on the Website ("third party cookies"). These third parties can recognize you when you visit our website and also when you visit certain other websites. You may learn more about cookies and how they work here: https://www.internetcookies.com/')
                    },
                    {
                    'subtitle': 'What type of cookies do we use?',
                    'subtext': mark_safe("- Necessary cookies<br />Necessary cookies allow us to offer you the best possible experience when accessing and navigating through our Website and using its features. For example, these cookies let us recognize that you have created an account and have logged into that account to access the content.<br />- Analytical cookies<br />These cookies enable us and third party services to collect aggregated data for statistical purposes on how our visitors use the Website. These cookies do not contain personal information such as names and email addresses and are used to help us improve your user experience of the Website.")
                    },
                    {
                    'subtitle': 'What are your cookie options?',
                    'subtext': mark_safe("If you don't like the idea of cookies or certain types of cookies, you can change your browser's settings to delete cookies that have already been set and to not accept new cookies. Visit internetcookies.com to learn more about how to do this.")
                    },
                    {
                    'subtitle': 'Changes and amendments',
                    'subtext': mark_safe("We reserve the right to modify this Policy or its terms relating to the Website and Services at any time, effective upon posting of an updated version of this Policy on the Website. When we do, we will revise the updated date at the bottom of this page. Continued use of the Website and Services after any such changes shall constitute your consent to such changes.")
                    },
                    {
                    'subtitle': 'Acceptance of this policy',
                    'subtext': mark_safe("You acknowledge that you have read this Policy and agree to all its terms and conditions. By accessing and using the Website and Services you agree to be bound by this Policy. If you do not agree to abide by the terms of this Policy, you are not authorized to access or use the Website and Services.")
                    },
                    {
                    'subtitle': 'Contacting us',
                    'subtext': mark_safe('If you would like to contact us to understand more about this Policy or wish to contact us concerning any matter relating to our use of cookies, you may contact us using the "Contact Form" located in the homepage.')
                    },
                    ],
            },
            'job_seekers_policy': {
                'title': 'Privacy Policy For Job Applicants',
                'introduction': 'This job seekers policy explains who processes your data and how long it is kept before is being deleted.',
                'contents': [
                    {
                    'subtitle': 'Who is responsible for processing?',
                    'subtext': mark_safe('NORTATEM Sàrl is responsible for the processing of personal data which you provide us with on your curriculum. In the present section the information about how we use your data and the rights which you have by virtue of the General Data Protection Regulation (GDPR) is provided.<br />If you have any questions regarding the processing of your personal data, us using the "Contact Form" located in the homepage. Likewise, we inform you that NORTATEM has a Data Protection Officer designated at group level, that will respond to your inquiry.')
                    },
                    {
                    'subtitle': 'What do we process your personal data for?',
                    'subtext': mark_safe("We process your personal data to manage your job application and your curriculum to be able to contact you when we have a position that suits your skills.")
                    },
                    {
                    'subtitle': 'What is the legitimacy for the processing of your personal data?',
                    'subtext': mark_safe("We will process your personal data on the legal basis of the legitimate interest of processing them in the different open contracting processes in which your professional profile fits according to the personal data that you have provided us with.")
                    },
                    {
                    'subtitle': 'To which recipients are your personal data communicated?',
                    'subtext': mark_safe("We will communicate your personal data to NORTATEM affiliates on the legal basis of legitimate interest for administrative purposes. On the other hand, service providers of NORTATEM systems or technologies will be able to access your personal data for the provision of our services.We will not make international data transfers outside the European Union.")
                    },
                    {
                    'subtitle': 'For how long do we keep your personal data?',
                    'subtext': mark_safe("The period during which we will process your personal data will depend on each process, establishing internally the relevant retention periods depending on the category of the position. Also, we often have offers on similar job positions at NORTATEM and its affiliates, we can store your data for the period that allows us to manage your potential application.")
                    },
                    {
                    'subtitle': 'What are your rights?',
                    'subtext': mark_safe('We inform you that you can exercise the following rights:<br />(i) right of access to your personal data to know which ones are being processed and the processing operations carried out with them;<br />(ii) right to rectify any inaccurate personal data;<br />(iii) right of deletion of your personal data, when this is possible;<br />(iv) right to request the limitation of the processing of your personal data when the accuracy, legality or the need for the processing of the data is doubtful, in which case, we may keep them for the exercise or defence of claims.<br />(v) right to oppose to the processing of your personal data, when the legal basis that enables us to process them is the legitimate interest. We will stop processing your data unless we have a legitimate interest or for the formulation, exercise or defence of claims.<br />You can exercise your rights at any time and for free by using the "Contact Form" located in the homepage indicating the right you wish to exercise and your personal identification information.<br />We inform you that you have the right to file a claim with the European Agency for Data Protection if you believe that a violation of the legislation on data protection regarding the processing of your personal data has been committed.')
                    },
                    {
                    'subtitle': 'Confidentiality',
                    'subtext': mark_safe('By attending our selection process, you hereby acknowledge and accept that all data, materials, evidence, exercises or tests that we provide about a job position or about NORTATEM or any of its affiliates, in any format (written, verbal codified, etc.) are confidential (the "Confidential Information"). Likewise, you are obligated to:<br/>– (i) not use the Confidential Information for any purpose other than the selection process,<br/>– (ii) not disclose, publish, disseminate or communicate said Confidential Information to any third party;<br/>– (iii) not use the Confidential Information for the development of projects for your own benefit or that of third parties, and<br/>– (iv) to immediately inform NORTATEM of any disclosure or unauthorized use of the information you are aware of.<br/>In case of breach, you recognize and accept the right of NORTATEM to initiate the appropriate legal actions to request the specific fulfilment of this obligation and the compensation of the damages and losses caused. The obligation of confidentiality will remain in force as long as you keep the Confidential Information and for a period of 2 years after their destruction or return.')
                    },
                ],
            },
        },
    })