#!/usr/bin/python3
"""
A simple templating program to generate invitations.
"""

def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template and attendee list.
    """
    # Giriş tiplərini yoxla
    if not isinstance(template, str):
        print("Error: template must be a string. Got: {}".format(type(template).__name__))
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    # Boş girişləri yoxla
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Hər iştirakçı üçün emal et
    for i, attendee in enumerate(attendees, start=1):
        processed_template = template
        
        # Placeholder-ləri əvəz et
        placeholders = ["name", "event_title", "event_date", "event_location"]
        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            processed_template = processed_template.replace("{" + key + "}", str(value))

        # Faylı yaz
        filename = "output_{}.txt".format(i)
        try:
            with open(filename, 'w') as f:
                f.write(processed_template)
        except Exception as e:
            print("Error writing to {}: {}".format(filename, e))

