from fastapi import FastAPI
import random

app = FastAPI()

side_hustle = [
    "Pet Sitting or Dog Walking - offer pet care services to busy pet owners in your community.",
    "Freelance Writing - write articles, blog posts, or copy for businesses and publications.",
    "Social Media Management - manage social media accounts for small businesses to enhance their online presence.",
    "Event Planning - organize events such as weddings, parties, or corporate functions.",
    "Personal Fitness Training - provide fitness coaching and training sessions to clients.",
    "Language Translation Services - translate documents or provide interpretation services for individuals or businesses.",
    "Handyman Services - offer repair and maintenance services for homes or offices.",
    "Baking and Cake Decorating - create custom cakes and baked goods for special occasions.",
    "Photography Services - capture special moments for clients, such as weddings or family portraits.",
    "Gardening and Landscaping - design and maintain gardens and outdoor spaces for clients.",
    "Etsy Seller - create and sell handmade crafts, jewelry, or digital art.",
    "Dropshipping - start an online store and sell products without holding inventory.",
    "Affiliate Marketing - promote products and earn commissions through referral links.",
    "Print on Demand - design custom t-shirts, mugs, or phone cases and sell online.",
    "Virtual Assistant - help businesses with admin tasks like email management and scheduling.",
    "Online Tutoring - teach subjects like math, English, or programming to students.",
    "Resume and Cover Letter Writing - assist job seekers in crafting professional resumes.",
    "Voice-Over Artist - record voice-overs for videos, ads, or audiobooks.",
    "Stock Photography - sell high-quality images on platforms like Shutterstock or Adobe Stock.",
    "NFTs & Digital Art - create and sell digital artwork as NFTs.",
    "Domain Flipping - buy and sell domain names for a profit.",
    "Video Editing - edit videos for YouTubers, influencers, and businesses.",
    "Podcasting - start a podcast and monetize through sponsorships and ads.",
    "T-shirt & Merch Design - sell custom designs on platforms like Redbubble or Teespring.",
    "Amazon KDP - self-publish books and earn royalties from Amazon.",
    "Web Development - build websites and landing pages for businesses.",
    "App Development - create and sell mobile or web apps.",
    "SEO Consulting - help businesses rank higher on Google.",
    "Online Surveys & Reviews - earn money by reviewing products and filling out surveys.",
    "Handwriting & Calligraphy - create handwritten letters and wedding invitations.",
    "Local Delivery Services - offer same-day delivery in your area.",
    "Flipping Used Electronics - buy and resell refurbished electronics.",
    "AI Chatbot Development - build chatbots for businesses using AI tools.",
    "Car Detailing - clean and polish cars for customers.",
    "Custom Illustration Services - draw custom artwork for clients.",
    "Travel Planning - help people plan their vacations and find the best deals.",
    "Event Photography - take professional photos at events and sell prints.",
    "3D Modeling - create 3D assets for games, AR/VR, and animations.",
    "Mystery Shopping - get paid to shop and review customer experiences.",
    "Copywriting - write compelling sales copies, blogs, and social media content.",
    "Music Production - compose and sell beats or background music.",
    "Website Flipping - buy, improve, and sell websites for profit.",
    "Resume Writing - help people create professional resumes and cover letters.",
    "Digital Marketing - manage online ad campaigns for businesses."
]

money_quotes = [
    "Don't work for money; make money work for you. - Robert Kiyosaki",
    "Rich people have small TVs and big libraries, and poor people have small libraries and big TVs. - Zig Ziglar",
    "Time is more valuable than money. You can get more money, but you cannot get more time. - Jim Rohn",
    "It’s not about having lots of money. It’s about knowing how to manage it. - Unknown",
    "If you don’t find a way to make money while you sleep, you will work until you die. - Warren Buffett",
    "Money is a terrible master but an excellent servant. - P.T. Barnum",
    "Financial freedom is available to those who learn about it and work for it. - Robert Kiyosaki",
    "Wealth is the ability to fully experience life. - Henry David Thoreau",
    "The key to making money is to stay invested. - Suze Orman",
    "Make money, not excuses. - Grant Cardone",
    "Do what you love, and the money will follow. - Marsha Sinetar",
    "Money grows on the tree of persistence. - Japanese Proverb",
    "A wise person should have money in their head, but not in their heart. - Jonathan Swift",
    "Do not save what is left after spending, but spend what is left after saving. - Warren Buffett",
    "An investment in knowledge pays the best interest. - Benjamin Franklin",
    "A budget is telling your money where to go instead of wondering where it went. - Dave Ramsey",
    "Opportunity is missed by most people because it is dressed in overalls and looks like work. - Thomas Edison",
    "The real measure of your wealth is how much you'd be worth if you lost all your money. - Unknown",
    "If you want to be rich, stop asking for permission. - Unknown",
    "The only way to become rich is to add more value to others than anyone else does. - Tony Robbins"
]


@app.get("/side_hustle")
def get_side_hustle():
    """
    Get a random side hustle idea.
    """
    return {"side hustle": random.choice(side_hustle)}


@app.get("/money_quotes")
def get_money_quotes():
    """
    Get a random money quote.
    """
    return {"money quote": random.choice(money_quotes)}
