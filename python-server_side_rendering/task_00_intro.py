"""
    A function that generates an invitation from a template for attendees.

    Args:
        template (str): the template.
        attendees (list(dict)): the attendees.
        
    Returns:
        An invitation, written in an output file, in replacing
        each placeholders from the template.
"""
import os


def generate_invitations(template, attendees):
    """
        Verifies that template is a string
        and attendees is a list of dictionaries.
    """
    if not isinstance(template, str):
        print("Error: Template is not a string.")
        return
    if not isinstance(attendees, list):
        for attendee in attendees:
            if not isinstance(attendee, dict):
                print("Error: Attendees should be a list of dictionaries.")
                return

    """ Specific Error Handling Behaviors. """
    if not template:
        print("Error: Template is empty, no output files generated.")
        return
    if not attendees:
        print("Error: No data provided, no output files generated.")
        return

    """
        Iterates over the list of attendees and replace the placeholders
        in the template with the corresponding values from each attendee's
        dictionary.
    """
    for index, attendee in enumerate(attendees, start=1):
        invitation = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key) or "N/A"
            placeholder = "{" + key + "}"
            invitation = invitation.replace(placeholder, value)
        
        """
            Writes the processed template to output files named output_{index}.txt,
            where {index} is the index of the attendee starting from 1.
        """
        output_filename = f"output_{index}.txt"
        
        """ Checks if the output file already exists before writing. """
        if os.path.exists(output_filename):
            print(f"Error: The file {output_filename} already exists.")
            continue
        
        try:
            with open(output_filename, 'w') as file:
                file.write(invitation)
        except Exception as e:
            print(f"Error: Impossible to write to the file {output_filename}. Exception: {e}")
