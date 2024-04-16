async def process_booking(booking):
    result = {         
        "customer_name": booking.contact_details.name,         
        "customer_age": booking.contact_details.age,         
        "customer_email": booking.contact_details.email,         
        "customer_phone": booking.contact_details.phone,         
        "flight_origin": booking.flight_details.origin,        
        "flight_destination": booking.flight_details.destination,         
        "flight_date": booking.flight_details.flight_date.strftime("%Y-%m-%d"),         
        # "customer_next_of_kin": booking.contact_details.next_of_kin,         
        "seat_preference": booking.seat_pref,   
    }     
    return result