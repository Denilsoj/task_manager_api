import os
from tasks.auth.google_auth import get_google_credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dotenv import load_dotenv
load_dotenv()



class Manage_google_calendar_event():

    @staticmethod
    def create(event_data):
        creds = get_google_credentials()
        service = build('calendar', 'v3', credentials=creds)

        event = {
            'summary': event_data['title'],
            'description': event_data.get('description', ''),
            'start': {
                'dateTime': event_data['start'],
                'timeZone': 'America/Sao_Paulo',
            },
            'end': {
                'dateTime': event_data['end'],
                'timeZone': 'America/Sao_Paulo',
            },
        }
        try:
            event_result = service.events().insert(
                calendarId = os.getenv('CALENDAR_ID', 'change-me'), 
                body=event
            ).execute()
            return {
                'status': 'success',
                'event_id': event_result['id'],
                'htmlLink': event_result.get('htmlLink'),
                'message': 'Event successfully created on Google Calendar'
            }
        
        except HttpError as error:
        
            return {
                'status': 'error',
                'message': 'Error creating event in Google Calendar',
                'details': str(error)
            }

        except Exception as e:
            
            return {
                'status': 'error',
                'message': 'Error creating event in Google Calendar',
                'details': str(e)
            }
        
    @staticmethod
    def delete(event_id):
        creds = get_google_credentials()
        service = build('calendar', 'v3', credentials=creds)

        try:
            service.events().delete(
                calendarId= os.getenv('CALENDAR_ID', 'change-me'),
                eventId=event_id
            ).execute()
            return {"status": "success", "message": f"Event {event_id} deletado com sucesso do Google Calendar."}

        except HttpError as error:
            
            return {"status": "error", "message": "Error when deleting event from Google Calendar.", "details": str(error)}

        except Exception as e:
            
        
            return {"status": "error", "message": "Error when deleting event from Google Calendar.", "details": str(e)}