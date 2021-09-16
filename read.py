import time
import datetime
import sqlite3
import pandas as pd

chat_id = ''; ## Must set Chat_ID as the targeted user you're receiving texts from. Must find in chat.db in macOS

#retrieves the most recent text message from user
def get_recent_messages(id):
    chat_id = id

    # Must set to your own directory to 'chat.db'
    conn = sqlite3.connect('/Users/kylehuynh/Library/Messages/chat.db')
    current = conn.cursor()

    messages = pd.read_sql_query(
        "SELECT * FROM message WHERE is_sent = 0 AND handle_id = {} ORDER BY date DESC limit 10".format(chat_id), conn)

    handles = pd.read_sql_query("select * from handle", conn)
    messages.rename(columns={'ROWID': 'message_id'}, inplace=True)

    handles.rename(columns={'id': 'phone_number',
                'ROWID': 'handle_id'}, inplace=True)

    merge_level_1 = temp = pd.merge(messages[['text', 'handle_id', 'date', 'is_sent',
                                            'message_id']], handles[['handle_id', 'phone_number']], on='handle_id', how='left')

    chat_message_joins = pd.read_sql_query("select * from chat_message_join", conn)

    # join back to the merge_level_1 dataframe
    clean_message = pd.merge(merge_level_1, chat_message_joins[[
                            'chat_id', 'message_id']], on='message_id', how='left')

    latest_text = clean_message.text[0]
    return latest_text 

    current.close()
    conn.close()


def current_message_id(id):
    chat_id = id
    conn = sqlite3.connect('/Users/kylehuynh/Library/Messages/chat.db')
    current = conn.cursor()

    messages = pd.read_sql_query(
        "SELECT * FROM message WHERE is_sent = 0 AND handle_id = {} ORDER BY date DESC limit 10".format(chat_id), conn)

    handles = pd.read_sql_query("select * from handle", conn)
    messages.rename(columns={'ROWID': 'message_id'}, inplace=True)

    handles.rename(columns={'id': 'phone_number',
                'ROWID': 'handle_id'}, inplace=True)

    merge_level_1 = temp = pd.merge(messages[['text', 'handle_id', 'date', 'is_sent',
                                            'message_id']], handles[['handle_id', 'phone_number']], on='handle_id', how='left')

    chat_message_joins = pd.read_sql_query("select * from chat_message_join", conn)

    # join back to the merge_level_1 dataframe
    clean_message = pd.merge(merge_level_1, chat_message_joins[[
                            'chat_id', 'message_id']], on='message_id', how='left')

    return clean_message.message_id[0]

    current.close()
    conn.close()
