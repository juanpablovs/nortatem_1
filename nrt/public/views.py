from django.shortcuts import render
from django.utils.safestring import mark_safe

navbar = {'titulo': 'el uno', 'otro': 'el dos'}
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
            'last_updated_msg': 'This document was last updated on',
            'privacy_policy': {
                'title': 'Privacy Policy',
                'introduction': 'This privacy policy ("Policy") describes how the personally identifiable information ("Personal Information") you may provide on the nortatem.com website ("NORTATEM" or "Service") and any of its related products and services (collectively, "Services") is collected, protected and used. It also describes the choices available to you regarding our use of your Personal Information and how you can access and update this information. This Policy is a legally binding agreement between you ("User", "you" or "your") and this Website operator ("Operator", "we", "us" or "our"). By accessing and using the Website and Services, you acknowledge that you have read, understood, and agree to be bound by the terms of this Policy. This Policy does not apply to the practices of companies that we do not own or control, or to individuals that we do not employ or manage.',
                'contents': [{
                    'subtitle': 'Automatic collection of information',
                    'subtext': mark_safe("When you open the Website, our servers automatically record information that your browser sends. This data may include information such as your device's IP address, browser type and version, operating system type and version, language preferences or the webpage you were visiting before you came to the Website and Services, pages of the Website and Services that you visit, the time spent on those pages, information you search for on the Website, access times and dates, and other statistics.<br />Information collected automatically is used only to identify potential cases of abuse and establish statistical information regarding the usage and traffic of the Website and Services. This statistical information is not otherwise aggregated in such a way that would identify any particular user of the system.")
                    },
                    {
                    'subtitle': 'Collection of personal information',
                    'subtext': mark_safe("You can access and use the Website and Services without telling us who you are or revealing any information by which someone could identify you as a specific, identifiable individual. If, however, you wish to use some of the features on the Website, you may be asked to provide certain Personal Information (for example, your name and e-mail address). We receive and store any information you knowingly provide to us when you create an account, publish content, or fill any online forms on the Website. When required, this information may include the following:<br />- Personal details such as name, country of residence, etc.<br />- Contact information such as email address, address, etc.<br />- Account details such as user name, unique user ID, password, etc.<br />- Geolocation data such as latitude and longitude.<br />Some of the information we collect is directly from you via the Website and Services. However, we may also collect Personal Information about you from other sources such as public databases and our joint marketing partners. You can choose not to provide us with your Personal Information, but then you may not be able to take advantage of some of the features on the Website. Users who are uncertain about what information is mandatory are welcome to contact us.")}],
            },
        },
    })