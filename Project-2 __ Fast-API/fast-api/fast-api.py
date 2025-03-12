from fastapi import FastAPI
import random

app = FastAPI()

side_hustle = [
    "App Development - create and sell mobile or web apps.",
    "Print on Demand - design and sell custom t-shirts, mugs, and more.",
    "Stock Photography - sell high-quality images on platforms like Shutterstock or Adobe Stock.",
    "Podcasting - start a podcast and monetize through sponsorships and ads.",
    "YouTube Channel - create videos and earn through ads, sponsorships, and affiliate links.",
    "NFTs & Digital Art - sell digital assets and artwork as NFTs.",
    "Domain Flipping - buy and sell domain names for profit.",
    "Voice Over Work - offer voice-over services for commercials, videos, and audiobooks.",
    "Online Tutoring - teach subjects or programming languages online.",
    "UI/UX Design - design user interfaces and experiences for websites and apps.",
    "SEO Consulting - help businesses rank higher on Google.",
    "Copywriting - write compelling sales copies, blogs, and social media content.",
    "Handmade Crafts - sell handmade products on Etsy.",
    "Video Editing - edit videos for YouTubers, influencers, and businesses.",
    "3D Modeling - create 3D assets for games, AR/VR, and animations.",
    "Online Surveys & Reviews - earn money by reviewing products and filling out surveys.",
    "Transcription Services - convert audio files into text.",
    "Data Entry - enter and manage data for businesses.",
    "Flipping Used Electronics - buy and resell refurbished electronics.",
    "T-shirt & Merch Design - create and sell merch on Redbubble or Teespring.",
    "Music Production - compose and sell beats or background music.",
    "Course Reselling - buy online course bundles and resell them for a profit.",
    "Local Delivery Services - offer same-day delivery in your area.",
    "Handwriting & Calligraphy - create handwritten letters and wedding invitations.",
    "AI Chatbot Development - build chatbots for businesses using AI tools.",
    "Amazon KDP - self-publish books and earn royalties from Amazon.",
    "Renting Equipment - rent out camera gear, laptops, or tools.",
    "Website Flipping - buy, improve, and sell websites for profit.",
    "Resume Writing - help people create professional resumes and cover letters.",
    "Digital Marketing - manage online ad campaigns for businesses."
]

money_quotes = [
    "Wealth consists not in having great possessions, but in having few wants. - Epictetus",
    "The stock market is filled with individuals who know the price of everything, but the value of nothing. - Philip Fisher",
    "Money often costs too much. - Ralph Waldo Emerson",
    "An investment in knowledge pays the best interest. - Benjamin Franklin",
    "Too many people spend money they haven't earned to buy things they don't want to impress people they don't like. - Will Rogers",
    "A wise person should have money in their head, but not in their heart. - Jonathan Swift",
    "Money grows on the tree of persistence. - Japanese Proverb",
    "Do not save what is left after spending, but spend what is left after saving. - Warren Buffett",
    "It is not the man who has too little, but the man who craves more, that is poor. - Seneca",
    "The real measure of your wealth is how much you'd be worth if you lost all your money. - Unknown",
    "Formal education will make you a living; self-education will make you a fortune. - Jim Rohn",
    "If you want to be rich, stop asking for permission. - Unknown",
    "Opportunity is missed by most people because it is dressed in overalls and looks like work. - Thomas Edison",
    "The only way to become rich is to add more value to others than anyone else does. - Tony Robbins",
    "A budget is telling your money where to go instead of wondering where it went. - Dave Ramsey",
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
