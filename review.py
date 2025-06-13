import json

# Sample dataset
products = [
    {"id": 1, "name": "Wireless Headphones", "price": 99.99, "category": "Electronics", "avg_rating": 4.3},
    {"id": 2, "name": "Smartphone X", "price": 699.99, "category": "Electronics", "avg_rating": 4.5},
    {"id": 3, "name": "Blender Pro", "price": 49.99, "category": "Home Appliances", "avg_rating": 4.1},
    {"id": 4, "name": "Running Shoes", "price": 79.99, "category": "Sports", "avg_rating": 4.6},
    {"id": 5, "name": "Coffee Maker", "price": 129.99, "category": "Kitchen", "avg_rating": 4.4},
    {"id": 6, "name": "Yoga Mat", "price": 29.99, "category": "Fitness", "avg_rating": 4.7},
    {"id": 7, "name": "Smart Watch", "price": 199.99, "category": "Electronics", "avg_rating": 4.2},
    {"id": 8, "name": "Backpack", "price": 59.99, "category": "Accessories", "avg_rating": 4.0},
    {"id": 9, "name": "Air Fryer", "price": 89.99, "category": "Kitchen", "avg_rating": 4.8},
    {"id": 10, "name": "Wireless Earbuds", "price": 129.99, "category": "Electronics", "avg_rating": 4.4}
]

reviews = [
    {"product_id": 1, "user": "Alex", "rating": 5, "comment": "Amazing sound quality!"},
    {"product_id": 1, "user": "Jamie", "rating": 4, "comment": "Great but battery life could be better"},
    {"product_id": 2, "user": "Taylor", "rating": 5, "comment": "Best phone I've ever owned"},
    {"product_id": 2, "user": "Casey", "rating": 4, "comment": "Excellent camera but a bit pricey"},
    {"product_id": 3, "user": "Morgan", "rating": 4, "comment": "Blends smoothly but noisy"},
    {"product_id": 4, "user": "Riley", "rating": 5, "comment": "Super comfortable for long runs"},
    {"product_id": 4, "user": "Jordan", "rating": 4, "comment": "Good traction but takes time to break in"},
    {"product_id": 5, "user": "Skyler", "rating": 5, "comment": "Makes perfect coffee every morning"},
    {"product_id": 6, "user": "Dakota", "rating": 5, "comment": "Thick and comfortable - no slipping"},
    {"product_id": 6, "user": "Quinn", "rating": 4, "comment": "Great mat but could be wider"},
    {"product_id": 7, "user": "Avery", "rating": 4, "comment": "Good features but battery drains fast"},
    {"product_id": 7, "user": "Peyton", "rating": 3, "comment": "Screen scratches too easily"},
    {"product_id": 8, "user": "Rowan", "rating": 4, "comment": "Durable and spacious"},
    {"product_id": 8, "user": "Sage", "rating": 2, "comment": "Zipper broke after 2 weeks"},
    {"product_id": 9, "user": "Emerson", "rating": 5, "comment": "Crispy fries with no oil - amazing!"},
    {"product_id": 9, "user": "Finley", "rating": 5, "comment": "Game changer for healthy cooking"},
    {"product_id": 10, "user": "Hayden", "rating": 4, "comment": "Good sound but case is bulky"},
    {"product_id": 10, "user": "Rory", "rating": 5, "comment": "Perfect fit and great noise cancellation"},
    {"product_id": 3, "user": "Shane", "rating": 3, "comment": "Average performance for the price"},
    {"product_id": 5, "user": "Jesse", "rating": 4, "comment": "Consistent results but takes up counter space"}
]

def get_product_name(product_id):
    for product in products:
        if product["id"] == product_id:
            return product["name"]
    return "Unknown Product"

def chatbot_response(message):
    message = message.lower().strip()

    # Greeting
    if any(word in message for word in ["hi", "hello", "hey"]):
        return "Hello! I'm your Product Review Assistant. 😊 How can I help you today?"

    # Help/Options
    elif "help" in message or "what can you do" in message:
        return (
            "I can help you with:\n"
            "- Leave a product review (say 'leave review')\n"
            "- Read existing reviews (say 'view reviews')\n"
            "- Edit or delete your review (say 'edit review')\n"
            "- Get recommendations (say 'recommendations')\n"
            "- Report a review (say 'report review')\n"
            "Just tell me what you need!"
        )

    # Leave a review (COMPLETE FLOW)
    elif any(word in message for word in ["leave review", "add review", "write review"]):
        print("\nAvailable products:")
        for product in products:
            print(f"{product['id']}. {product['name']} (${product['price']})")

        try:
            product_id = int(input("\nWhich product are you reviewing? (Enter ID): "))
            if not any(p["id"] == product_id for p in products):
                return "❌ Invalid product ID. Please try again."
        except ValueError:
            return "❌ Please enter a number (e.g., 1, 2, 3)."

        user = input("Your name: ")
        try:
            rating = int(input("Rating (1-5 stars): "))
            if rating < 1 or rating > 5:
                return "❌ Rating must be between 1-5."
        except ValueError:
            return "❌ Please enter a number (e.g., 4)."

        comment = input("Your review comment (optional): ")
        reviews.append({"product_id": product_id, "user": user, "rating": rating, "comment": comment})
        return f"✅ Thanks {user}! Your review for {get_product_name(product_id)} has been submitted."

    # View reviews (FIXED - NO NAME PROMPT)
    elif any(word in message for word in ["view reviews", "see reviews", "read reviews"]):
        print("\nAvailable products:")
        for product in products:
            print(f"{product['id']}. {product['name']}")

        try:
            product_id = int(input("\nEnter product ID to view reviews: "))
            if not any(p["id"] == product_id for p in products):
                return "❌ Invalid product ID. Please try again."
        except ValueError:
            return "❌ Please enter a number (e.g., 1, 2, 3)."

        product_reviews = [r for r in reviews if r["product_id"] == product_id]
        if not product_reviews:
            return f"🌟 No reviews yet for {get_product_name(product_id)}. Be the first!"

        response = f"\n📝 Reviews for {get_product_name(product_id)}:\n"
        for review in product_reviews:
            response += f"👤 {review['user']} ⭐ {review['rating']}: {review['comment']}\n"
        return response

    # Edit/Delete review
    elif any(word in message for word in ["edit review", "delete review", "change review"]):
        user = input("\nTo manage your reviews, please enter your name: ")
        user_reviews = [r for r in reviews if r["user"].lower() == user.lower()]

        if not user_reviews:
            return f"❌ No reviews found under '{user}'. Did you use a different name?"

        print("\nYour reviews:")
        for i, review in enumerate(user_reviews):
            print(f"{i+1}. {get_product_name(review['product_id'])} ⭐ {review['rating']}: {review['comment']}")

        try:
            choice = int(input("\nEnter review number to edit/delete (0 to cancel): "))
            if choice == 0:
                return "Operation cancelled."
            if choice < 1 or choice > len(user_reviews):
                return "❌ Invalid selection."
        except ValueError:
            return "❌ Please enter a number."

        selected_review = user_reviews[choice-1]
        action = input("Edit (E) or Delete (D)? ").upper()

        if action == "E":
            try:
                new_rating = int(input(f"New rating (current: {selected_review['rating']}): "))
                if new_rating < 1 or new_rating > 5:
                    return "❌ Rating must be 1-5."
            except ValueError:
                return "❌ Please enter a number."

            new_comment = input(f"New comment (current: {selected_review['comment']}): ")
            selected_review["rating"] = new_rating
            selected_review["comment"] = new_comment
            return "✅ Review updated successfully!"
        elif action == "D":
            reviews.remove(selected_review)
            return "🗑️ Review deleted successfully!"
        else:
            return "❌ Invalid action. Please type 'E' or 'D'."

    # Recommendations
    elif any(word in message for word in ["recommend", "suggest", "best products"]):
        top_products = sorted(products, key=lambda x: x["avg_rating"], reverse=True)[:3]
        response = "\n🌟 Top Rated Products:\n"
        for product in top_products:
            response += f"⭐ {product['avg_rating']} - {product['name']} (${product['price']})\n"
        return response

    # Report review
    elif any(word in message for word in ["report", "fake review", "inappropriate"]):
        print("\nAvailable products:")
        for product in products:
            print(f"{product['id']}. {product['name']}")

        try:
            product_id = int(input("\nEnter product ID with the review to report: "))
            if not any(p["id"] == product_id for p in products):
                return "❌ Invalid product ID."
        except ValueError:
            return "❌ Please enter a number."

        product_reviews = [r for r in reviews if r["product_id"] == product_id]
        if not product_reviews:
            return f"❌ No reviews found for {get_product_name(product_id)}."

        print(f"\nReviews for {get_product_name(product_id)}:")
        for i, review in enumerate(product_reviews):
            print(f"{i+1}. 👤 {review['user']}: {review['comment']}")

        try:
            choice = int(input("\nEnter review number to report (0 to cancel): "))
            if choice == 0:
                return "Report cancelled."
            if choice < 1 or choice > len(product_reviews):
                return "❌ Invalid selection."
        except ValueError:
            return "❌ Please enter a number."

        reason = input("Reason (spam/inappropriate/fake): ")
        return f"🚨 Thank you! Review reported for '{reason}'. Our team will investigate."

    # Exit
    elif any(word in message for word in ["bye", "exit", "quit"]):
        return "👋 Goodbye! Come back anytime for product help."

    # Fallback
    else:
        return (
            "🤔 I didn't understand that. Try:\n"
            "- 'Leave review' to add feedback\n"
            "- 'View reviews' to read comments\n"
            "- 'Edit review' to update yours\n"
            "- 'Recommendations' for top products\n"
            "- 'Report review' to flag issues"
        )

# Main chat loop
print("🛍️ Welcome to the Product Review Assistant! Type 'help' for options.")
while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ["bye", "exit", "quit"]:
        print("Chatbot: 👋 Goodbye! Have a great day!")
        break
    response = chatbot_response(user_input)
    print(f"Chatbot: {response}")