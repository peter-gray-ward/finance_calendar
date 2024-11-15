from enum import Enum

class Frequency(Enum):
  DAILY = 'daily'
  WEEKLY = 'weekly'
  BIWEEKLY = 'biweekly'
  MONTHLY = 'monthly'
  YEARLY = 'yearly'

class Range(Enum):
  TMR = "tmr"

class Page(Enum):
    CALENDAR = 1
    DAY = 2
    PREVIOUSMONTH = 3
    NEXTMONTH = 4
    EVENT = 5
    PRESENTS = 6
    IMAGINE = 7
    LEFTPANEL = 8
    RIGHTPANEL = 9,
    DAILYNEWS = 11

Api = {
  'ADD_EXPENSE': 'add-expense',
  'DELETE_EXPENSE': 'delete-expense',
  'UPDATE_EXPENSE': 'update-expense',
  'REFRESH_CALENDAR': 'refresh-calendar',
  'CHANGE_MONTH_YEAR': 'update-month-year',
  'GET_EVENT': 'get-event',
  'SAVE_THIS_EVENT': 'save-this-event',
  'SAVE_THIS_AND_FUTURE_EVENTS': 'save-this-and-future-events',
  'SAVE_CHECKING_BALANCE': 'save-checking-balance',
  'ADD_DEBT': 'add-debt',
  'UPDATE_DEBT': 'update-debt',
  'DELETE_DEBT': 'delete-debt',
  'CREATE_PAYMENT_PLAN': 'create-payment-plan',
  'CLUDE_THIS_EVENT': 'clude-this-event',
  'CLUDE_ALL_THESE_EVENTS': 'clude-all-these-events',
  'DELETE_THIS_EVENT': 'delete-this-event',
  'DELETE_ALL_THESE_EVENTS': 'delete-all-these-events',
  'ADD_EVENT': 'add-event'
}


frequency = [
  'daily',
  'weekly',
  'biweekly',
  'monthly',
  'yearly'
]

event_fields = [
    'recurrenceid', 
    'summary', 
    'date', 
    'recurrenceenddate', 
    'amount', 
    'total', 
    'balance', 
    'exclude', 
    'frequency'
]