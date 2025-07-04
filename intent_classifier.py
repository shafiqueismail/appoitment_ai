from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
import os

# 1. Structured training data
training_data = {
    "book_cleaning": [
    "I need to book a teeth cleaning",
    "Please schedule my dental cleaning",
    "I want to set up a cleaning appointment",
    "I'd like to schedule a cleaning visit",
    "Can you book me for a cleaning?",
    "Time to clean my teeth, book me in",
    "Help me get a cleaning appointment",
    "I’m looking to book a cleaning",
    "Book a visit for tooth cleaning",
    "When’s the next available cleaning slot?",
    "I need to come in for a cleaning",
    "Please help me schedule my teeth cleaning",
    "Can I arrange a cleaning session?",
    "How do I book a cleaning?",
    "Put me on the list for a cleaning",
    "I'd like a cleaning soon",
    "Book a professional cleaning for me",
    "Please add me for a cleaning",
    "I want to get my teeth cleaned this week",
    "Book me in for a hygiene appointment",
    "I’d like a basic cleaning",
    "I need to get plaque removed",
    "How can I book a cleaning session?",
    "I want a dentist cleaning slot",
    "Can I book an appointment for plaque removal?",
    "Schedule a hygiene cleaning please",
    "Reserve a spot for my dental cleaning",
    "I want to clean my teeth at the clinic",
    "I'd like to schedule oral cleaning",
    "Can you arrange a cleaning for me?",
    "Please put me down for a teeth cleaning",
    "Is there a cleaning appointment available?",
    "I’m due for a hygiene cleaning",
    "I'd like to book an appointment to clean my teeth",
    "Add me to the schedule for a cleaning",
    "I want to remove buildup on my teeth",
    "Need an appointment for plaque cleanup",
    "Time to clean up my teeth, can I book?",
    "I'd like to schedule a hygiene visit",
    "Book me a slot for professional cleaning",
    "Is there a spot for cleaning tomorrow?",
    "Can I get in for a cleaning this week?",
    "I need to get my dental cleaning done",
    "Teeth cleaning booking please",
    "Clean my teeth — book me in",
    "I'd like to visit for oral hygiene",
    "Can I get my cleaning soon?",
    "Please schedule me a quick cleaning",
    "I'd love to book a cleaning",
    "Can I do a cleaning before Friday?",
    "Let’s book a teeth cleaning session",
    "I want to book"
],
   "book_whitening": [
    "I'd like to schedule a whitening treatment",
    "I need to book a whitening session",
    "Book a time to whiten my teeth",
    "Please set an appointment for whitening",
    "Can I come in for a whitening service?",
    "I want to book a teeth whitening slot",
    "I need an appointment for whitening",
    "I’m looking to whiten my teeth",
    "I'd like to come in for whitening",
    "Let me schedule whitening for this week",
    "I’m ready to whiten my teeth now",
    "Is whitening available today?",
    "Can you help me book whitening?",
    "I want a whitening consultation",
    "Book my whitening treatment",
    "Put me down for teeth whitening",
    "I want to whiten my teeth professionally",
    "Can I reserve a whitening session?",
    "I'd like to do a whitening procedure",
    "Please help me set up a whitening",
    "Teeth whitening appointment, please",
    "I'd like an appointment to brighten my teeth",
    "Book me for a smile whitening",
    "I need to remove stains from my teeth",
    "Can I get a whitening consult?",
    "When can I do a whitening session?",
    "I'd like to book a cosmetic whitening service",
    "Do you have a whitening appointment open?",
    "I'd like a whitening procedure scheduled",
    "How soon can I come in for whitening?",
    "I want brighter teeth, book me in",
    "Schedule me for a whitening treatment",
    "Book whitening for next week please",
    "Add me to the whitening schedule",
    "Whitening service booking, please",
    "Help me whiten my smile",
    "I’m ready for a whitening treatment",
    "Whitening visit — can I book?",
    "I want to brighten my teeth with you",
    "Sign me up to whiten my teeth",
    "I'd love to get a teeth whitening session",
    "Please schedule me for whitening soon",
    "I’m interested in scheduling teeth whitening",
    "Book whitening treatment slot please",
    "Set a time for teeth whitening",
    "I'd like to start with a whitening procedure",
    "Can I get a whitening done tomorrow?",
    "I want your whitening service",
    "Book me for stain removal session",
    "I want a teeth whitening visit",
    "Do you do teeth whitening"
],
   "cancel_appointment": [
    "I want to cancel my visit",
    "Please cancel my upcoming appointment",
    "I can't come anymore, cancel it",
    "Can I cancel my slot?",
    "Cancel my visit to the dentist",
    "I’m no longer available, cancel the booking",
    "I have to cancel the appointment",
    "I won't be able to make it, cancel please",
    "Just cancel my appointment",
    "Can you take me off the schedule?",
    "Cancel my dental visit",
    "I don’t need the appointment anymore",
    "Please remove me from the schedule",
    "I want to cancel my slot",
    "I changed my mind, please cancel",
    "Don’t need the appointment now, cancel it",
    "Please cancel my reservation",
    "I want to cancel my time slot",
    "I’ll skip the appointment, cancel it",
    "Can I stop my appointment?",
    "No longer attending, please cancel",
    "Cancel the dental checkup I booked",
    "I can’t make it, cancel my visit",
    "Remove my name from the list",
    "Please take me off for today",
    "I’ve decided to cancel",
    "Can you drop my appointment?",
    "I want to call off my appointment",
    "Can I undo my booking?",
    "Cancel my upcoming cleaning",
    "Cancel my scheduled appointment please",
    "I’m cancelling my appointment",
    "I won't show up, cancel it",
    "Can you erase my booking?",
    "Forget the appointment, cancel it",
    "Don’t book me anymore",
    "Cancel my spot at the clinic",
    "No longer need the visit, cancel",
    "Call off my dental appointment",
    "Remove my cleaning from the schedule",
    "Please delete my dentist visit",
    "Take me off your schedule",
    "Cancel the booking I made yesterday",
    "I can’t make it, so cancel it",
    "I’m not coming anymore, cancel",
    "Cancel me for today",
    "Don’t count me in for the appointment",
    "Can you drop me from the list?",
    "I'm unavailable, cancel my slot",
    "Forget about my appointment"
],
    "reschedule_appointment": [
    "Can I change my appointment to another day?",
    "I'd like to reschedule my visit",
    "Can I move my checkup to next week?",
    "Is it possible to push my appointment?",
    "Please help me reschedule",
    "Can I adjust my booking?",
    "I won’t make it, can we reschedule?",
    "I need to move the date of my appointment",
    "Can I come another time instead?",
    "I can’t make the original time, need to reschedule",
    "Let’s move my appointment to Monday",
    "I’d prefer a later date for my cleaning",
    "I want to reschedule to a more convenient time",
    "My plans changed, I need a new slot",
    "I’m busy that day, can I get a new time?",
    "Can we shift the time of my cleaning?",
    "I need to postpone my appointment",
    "Something came up, can I move my dental visit?",
    "I want to change the day of my appointment",
    "Please reschedule my visit for next week",
    "I can't come at that time, let’s rebook",
    "I need to move my appointment by a few hours",
    "Can you help me reschedule for a later date?",
    "Let’s set my appointment for another time",
    "I’m running late, can we reschedule?",
    "I’ll be out of town, move my appointment please",
    "Can we change my cleaning to a different day?",
    "Please give me a new time for my checkup",
    "Can I get another slot for the same appointment?",
    "Reschedule my appointment to next Friday",
    "Can I come in the following week instead?",
    "I missed my appointment, can we move it?",
    "I had an emergency, need to reschedule",
    "Can you push my appointment to later?",
    "Please update the appointment time",
    "Can you cancel and rebook it for later?",
    "I need to switch my appointment date",
    "I want to reschedule to a weekend",
    "Can I do it another day?",
    "I need to find a different time for my appointment",
    "Please update my visit to another time",
    "Can you help me shift it to a later time?",
    "Let’s move it to Thursday if that’s okay",
    "Is there a better time for me?",
    "I want to choose another appointment day",
    "Push my visit back by a few days",
    "Let’s reschedule for a better time",
    "Please book me for a different time",
    "I can’t do that time, change it please",
    "I want to move my checkup to a different date",
    "Can you give me a later appointment?",
    "Reschedule to whenever the next slot is"
],
   "book_checkup": [
    "I need to schedule a checkup soon",
    "Can I come in for a routine checkup?",
    "I’d like to get my teeth checked",
    "Can you book me for a regular checkup?",
    "Please set up a dental checkup for me",
    "I think it's time for a checkup",
    "When can I do my yearly checkup?",
    "I’m due for a checkup, book me in",
    "I want to see the dentist for a quick check",
    "I’d like to come in for a dental exam",
    "Can I book an appointment for a general checkup?",
    "Help me book a dental evaluation",
    "I want to do my annual checkup",
    "Schedule a regular dentist visit for me",
    "I need an oral health checkup",
    "Can you add me for a dental check?",
    "I need my teeth looked at",
    "Please book me a regular dental check",
    "It’s time for a routine exam",
    "Can I get a quick checkup slot?",
    "I’m due for my 6-month checkup",
    "I want to check the condition of my teeth",
    "Let’s book a dentist exam",
    "I want to book a follow-up checkup",
    "I’m looking for a basic checkup",
    "Book my next dentist checkup",
    "Time for a checkup — can I book?",
    "Please schedule me for my next exam",
    "I think it's time for another dental check",
    "I’d like to make a checkup appointment",
    "When is my next dental checkup due?",
    "Set me up with a teeth check appointment",
    "How do I book a routine dental check?",
    "Book me for a dentist visit",
    "Can I have a quick oral exam?",
    "I just want to get my teeth checked",
    "Book a time for my general dental check",
    "I need an exam to check my teeth",
    "I want to make a dentist checkup",
    "When is the next time I can do a checkup?",
    "I want to come in just to get my teeth checked",
    "Let me book a simple dental check",
    "I want to check if my teeth are healthy",
    "How can I book a routine visit?",
    "I need a checkup before school starts",
    "I think I’m due for an oral exam",
    "Book my regular dental check slot",
    "I want a basic cleaning and checkup",
    "Check my teeth, can I book for that?",
    "Please sign me up for a regular exam",
    "I’m interested in a dental review appointment",
    "I just want to make sure my teeth are okay"
],
    "ask_price" : [
        "How much does it cost for a dental cleaning?",
        "What do you charge for whitening?",
        "Is a checkup expensive?",
        "Can I get a price list?",
        "I want to know the price of a filling",
        "How much would a root canal be?",
        "Do you accept insurance?",
        "What’s the cost of a teeth cleaning?",
        "How much does a checkup usually cost?",
        "Tell me the price for a dental exam",
        "How much will whitening cost me?",
        "Can you tell me your rates?",
        "What’s the fee for a regular cleaning?",
        "What are your prices like?",
        "How expensive is it to whiten teeth?",
        "Are your services affordable?",
        "What does a dental visit cost?",
        "Do you have pricing for all treatments?",
        "Tell me the cost of dental work",
        "How much do you charge for appointments?",
        "Do you have a consultation fee?",
        "What are your prices for cleanings?",
        "How much is a full checkup?",
        "Are checkups covered by insurance?",
        "What’s the average cost of a visit?",
        "Can I see a price estimate?",
        "How much money will I need for whitening?",
        "What’s your rate for dental services?",
        "How much do your appointments run?",
        "Is there a cost for booking?",
        "What’s the price for kids’ cleanings?",
        "How much is a fluoride treatment?",
        "Can you break down your pricing?",
        "How much do you charge for dental X-rays?",
        "What’s the cost for routine cleaning?",
        "How expensive is a new patient exam?",
        "Do you charge extra for polishing?",
        "Is insurance required to reduce the cost?",
        "What’s your rate for tooth extractions?",
        "Can I pay with insurance for cleaning?",
        "What’s the pricing for braces?",
        "Are your prices fixed?",
        "What’s the price difference with and without insurance?",
        "Is there a student discount?",
        "How much do fillings usually cost?",
        "Is whitening part of the cleaning price?",
        "How much does an appointment usually cost?",
        "Can I get a quote for a checkup?",
        "How much does a consultation cost?",
        "Do you charge for no-shows?",
        "What’s the total cost of a cleaning and exam?",
        "Are your services billed per visit?",
        "Can I get a discount for paying cash?",
        "Do you offer payment plans?",
        "How much would it be without insurance?",
        "Are emergency visits more expensive?",
        "What’s your pricing policy?",
        "How much is the first visit?",
        "Can you tell me the cost breakdown?",
        "How much is a routine appointment?",
        "Are prices different on weekends?",
        "What do you charge for gum treatment?",
        "Is teeth whitening included in cleaning?",
        "What’s the rate for a full dental exam?",
        "How much do you charge per service?",
        "Is the price different for kids?",
        "How much would I pay for whitening?",
        "How much for just a cleaning, no exam?",
        "How much is it to remove plaque?",
        "What’s the cost for annual dental care?",
        "Are there extra fees I should know about?",
        "How do you price your appointments?",
        "What’s the cost of a full dental evaluation?",
        "How much does dental care cost here?",
        "Can you share your treatment costs?",
        "Do I need to pay upfront?",
        "Can you estimate the price of my visit?",
        "Do you offer free checkups?",
        "How much is teeth polishing?",
        "Do prices vary per doctor?",
        "Can you show me your pricing options?",
        "How much is a professional cleaning?",
        "Is whitening covered by insurance?",
        "Do prices change by season?",
        "What’s the current rate for cleanings?",
        "Is your price list online?",
        "How much should I expect to pay?",
        "How much do extra services cost?",
        "Do you offer free consultations?",
        "Is there a flat fee for exams?",
        "How much do I pay for a dental appointment?",
        "What’s the usual cost for whitening?",
        "Do you charge hourly?",
        "What is the price to clean teeth professionally?",
        "Can I see your cost per procedure?",
        "Do I pay more if I have no insurance?",
        "Are cleaning prices different for adults and kids?",
        "Do you offer bundled pricing?",
        "Can you give me a pricing estimate?",
        "How are your cleaning services priced?",
        "Do I pay more for a deep cleaning?",
        "How much do exams and cleanings cost together?",
        "How much does a basic dental visit cost?",
        "What’s your rate per visit?",
        "Do you provide low-cost options?",
        "Can you email me your pricing?",
        "What’s the total price if I get cleaning and x-rays?"
],
    "ask_availability": [
    "What appointment slots do you have?",
    "When’s your next available time?",
    "Do you have anything open this afternoon?",
    "What days are you available this week?",
    "When can I schedule something?",
    "Can I come in this weekend?",
    "Are you open on Saturday?",
    "Let me know what times are free",
    "Do you have anything early in the morning?",
    "Can I book something this evening?",
    "Any spots open today?",
    "Are you free on Monday?",
    "Is there an appointment time available right now?",
    "What’s your soonest available slot?",
    "When can I come in for a visit?",
    "Do you have any evening availability?",
    "Can I get an appointment before noon?",
    "Are mornings better for scheduling?",
    "What’s your schedule look like today?",
    "Can I get a spot this week?",
    "Are there any free appointments tomorrow?",
    "What are your available times?",
    "I’m looking for your open hours",
    "What days do you take appointments?",
    "Is there anything open next week?",
    "When’s the earliest I can come?",
    "Can I book something right away?",
    "What’s your calendar like?",
    "Can I come on Tuesday morning?",
    "Any chance you have a spot on Thursday?",
    "Do you take late appointments?",
    "When do you have room for a cleaning?",
    "I want to know your free times",
    "Is Friday morning available?",
    "When can I see the dentist?",
    "I need something midweek, what’s open?",
    "Do you have any open slots soon?",
    "What’s your next availability?",
    "Is anything available in the next few days?",
    "Can I book a spot this afternoon?",
    "Do you work on Sundays?",
    "What’s the best time you have open?",
    "Are appointments available this month?",
    "Do you have a free time next Thursday?",
    "I want to come in this week — when can I?",
    "What day can you fit me in?",
    "Are you free any time this weekend?",
    "Can I get in tomorrow morning?",
    "When’s the earliest available cleaning?",
    "What time slots are still open?",
    "Do you take appointments after 5 PM?",
    "Is your schedule open next Wednesday?",
    "Do you have walk-in times or open slots?"
],
    "tooth_pain": [
    "My tooth is aching a lot",
    "I'm getting tooth pain when I eat",
    "There's a sharp pain in my back molar",
    "My gums are swollen and sore",
    "I feel pressure in my jaw",
    "My tooth hurts when I drink cold water",
    "I'm having nonstop pain in one tooth",
    "I think I cracked a tooth",
    "It hurts when I bite down",
    "My teeth are super sensitive lately",
    "I'm experiencing throbbing tooth pain",
    "The left side of my mouth really hurts",
    "My jaw feels sore near my molars",
    "There's pain under one of my crowns",
    "I can’t sleep because of the toothache",
    "I feel a stinging pain in my tooth",
    "One of my fillings feels loose and painful",
    "My gum is inflamed and painful",
    "I think I have an abscess",
    "There’s a bump on my gum and it hurts",
    "My wisdom teeth are really hurting",
    "My mouth feels sore and tender",
    "Pain is radiating from my jaw to my ear",
    "My tooth is hurting badly after eating sweets",
    "I think something's wrong with my root canal",
    "My whole face hurts on one side",
    "There’s pain when I touch my tooth",
    "My tooth is bleeding after brushing",
    "I think my tooth is infected",
    "It hurts to chew on one side",
    "There’s a bad taste coming from a sore tooth",
    "My tooth feels loose and painful",
    "Pain in my gum after flossing",
    "I feel heat sensitivity in my tooth",
    "The pain in my tooth is getting worse",
    "I feel throbbing under my crown",
    "I get a sharp jolt when I drink cold water",
    "My jaw pain is spreading to my temple",
    "I can't eat on one side because of pain",
    "One tooth is really bothering me today",
    "I bit something and now my tooth hurts",
    "I feel pressure around one of my teeth",
    "My dental bridge is hurting my gum",
    "I need help with serious mouth pain",
    "My molars hurt when I wake up",
    "I have pain after a dental procedure",
    "I feel soreness in my lower gum",
    "The pain keeps coming and going",
    "There’s pain when I touch the side of my face",
    "I feel discomfort after biting hard food",
    "Pain is worsening every hour",
    "My cheek is swollen from tooth pain",
    "I might have nerve pain in my tooth"
],
    "general_inquiry": [
    "What services are available at your clinic?",
    "Do you take new patients?",
    "Where are you located?",
    "Is your clinic open on Saturdays?",
    "How can I reach your office?",
    "Do you accept walk-in patients?",
    "Do you install braces?",
    "What kind of dental whitening do you offer?",
    "Is your clinic child-friendly?",
    "Can I have your contact number?",
    "Are consultations free?",
    "Do you have weekend hours?",
    "Can I visit without an appointment?",
    "Do you offer orthodontic care?",
    "What dental procedures do you do?",
    "What are your hours of operation?",
    "Do you treat toddlers?",
    "Can I call to ask questions?",
    "Do you provide cosmetic dentistry?",
    "What kind of insurance do you accept?",
    "Do you do extractions?",
    "Is your clinic accessible for disabled patients?",
    "Do you offer cleanings and exams?",
    "Can you tell me about your staff?",
    "Do you have multiple dentists?",
    "Do you take patients without insurance?",
    "Can I get a tour of your clinic?",
    "Do you treat dental emergencies?",
    "Are dental x-rays included in a checkup?",
    "What dental plans do you accept?",
    "Is your clinic busy usually?",
    "What types of treatments do you offer?",
    "Do you offer pediatric dentistry?",
    "Can I speak to a hygienist?",
    "Are you open on public holidays?",
    "Do you use modern equipment?",
    "Can I come in just to ask questions?",
    "What are your qualifications?",
    "Do you have parking available?",
    "Is your clinic near public transit?",
    "Do you offer sedation for anxious patients?",
    "What’s your cancellation policy?",
    "How many years have you been in practice?",
    "Are your services safe for pregnant women?",
    "Do you provide aftercare instructions?",
    "Is there a waiting list for appointments?",
    "Do you accept referrals?",
    "How long does a visit usually take?",
    "Are you open in the evenings?",
    "Do you have bilingual staff?"
],
   "out_of_scope": [
    "What’s the weather like tomorrow?",
    "Order me a pizza online",
    "How do I boil pasta?",
    "Tell me a funny joke",
    "My phone won’t charge",
    "What’s 45 divided by 5?",
    "Book me a flight to New York",
    "I need help with math homework",
    "What time is it in London?",
    "Is this a bakery?",
    "What’s the capital of Italy?",
    "How do I reset my laptop?",
    "Recommend a good restraunt",
    "Where can I buy running shoes?",
    "Turn off my smart lights",
    "Open YouTube for me",
    "Can you teach me to code?",
    "What’s the latest iPhone?",
    "Is soccer popular in Spain?",
    "How much does gas cost today?",
    "How do I unclog a sink?",
    "Can you set a timer?",
    "What is 7 x 9?",
    "Play some background music",
    "What's a good breakfast recipe?",
    "How do I find cheap flights?",
    "Show me today’s news headlines",
    "Can you check the stock market?",
    "Tell me a fun fact",
    "Translate ‘goodbye’ to Spanish",
    "How tall is the Eiffel Tower?",
    "How many states are in the USA?",
    "Remind me to take a walk later",
    "How do I install Zoom?",
    "What's trending on YouTube?",
    "Where is the closest train station?",
    "Can you play relaxing sounds?",
    "How do I bake cookies?",
    "Help me plan a vacation",
    "Is the mall open today?",
    "How many hours in a day?",
    "What’s a good TV show to binge?",
    "Can you give me directions?",
    "How fast can a cheetah run?",
    "What’s the deepest ocean?",
    "When was the Great Wall built?",
    "Can you open my camera app?",
    "What’s the tallest building in the world?",
    "Do I need an umbrella today?",
    "How do I update my software?"
]
}

# 2. Flatten the data into two lists
training_sentences = []
training_labels = []

for label, sentences in training_data.items():
    training_sentences.extend(sentences)
    training_labels.extend([label] * len(sentences))

# 3. Vectorize the text
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(training_sentences)

# 4. Train the model
model = MultinomialNB()
model.fit(X_train, training_labels)

# Save model and vectorizer for session memory
with open("model.pkl", "wb") as f: pickle.dump(model, f)
with open("vectorizer.pkl", "wb") as f: pickle.dump(vectorizer, f)

# 5. Intent → Response
intent_responses = {
    "book_cleaning": "We can book your dental cleaning. Would you like to continue?",
    "book_whitening": "Teeth whitening is available. Would you like to proceed?",
    "book_checkup": "Let's schedule your checkup. Should I continue?",
    "cancel_appointment": "Your appointment has been canceled. Let us know if you’d like to book again.",
    "reschedule_appointment": "Understood. When would you like to reschedule your appointment?",
    "ask_price": "Sure. I can help you with our service pricing. Which treatment are you interested in?",
    "ask_availability": "We’ll check what times are available. Do you have a preferred day or time?",
    "tooth_pain": "I'm sorry you're in pain. We recommend booking a visit. Would you like help with that?",
    "general_inquiry": "I'm happy to help with information about our services. What would you like to know?",
    "out_of_scope": "Sorry, I can only help with dental-related questions like appointments, services, or pricing.",
    "clarify_intent": "Sorry, I didn't quite understand. Could you please rephrase or be more specific?"
}

conversation_context = {
    "last_intent": None,
    "params": {},
    "history": []
}

# 6. Predict the intent    
def predict_intent(user_input):
    with open("model.pkl", "rb") as f: model = pickle.load(f)
    with open("vectorizer.pkl", "rb") as f: vectorizer = pickle.load(f)
    X_test = vectorizer.transform([user_input])
    prediction = model.predict(X_test)[0]
    confidence = model.predict_proba(X_test).max()
    return prediction, confidence

# 7. Response Engine with Flow Handling
def handle_response(user_input):
    prediction, confidence = predict_intent(user_input)
    context = conversation_context
    context["history"].append(user_input)

    if confidence < 0.5:
        return intent_responses["clarify_intent"]

    # Intent switch detection
    if context["last_intent"] and prediction != context["last_intent"]:
        context["last_intent"] = prediction
        context["params"] = {}
        return f"Okay, switching to {prediction.replace('_', ' ')}. {intent_responses[prediction]}"

    # Continue the current flow
    context["last_intent"] = prediction
    return intent_responses.get(prediction, "I'm not sure how to respond to that.")


# 8. Command Line Chat
if __name__ == "__main__":
    print("Welcome to the Dental Assistant AI. Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = handle_response(user_input)
        print("Assistant:", response, "\n")
