import streamlit as st
import pandas as pd
import requests

def main():
    # Define the GraphQL query
    query = '''
    query GetallApplications{
    allOpportunityApplication(
        page: 10
        per_page: 10
        filters: {
        person_home_mc : 1623
        person_home_lc : 222
        }
    ) {
        data {
        id
        status
        created_at
        date_approved
        date_realized
        experience_start_date
        experience_end_date
        date_approval_broken
        nps_response_completed_at
        updated_at
        person {
            id
            home_mc {
            id
            name
            }
            home_lc {
            id
            name
            }
        }
        host_lc {
            id
            name
        }
        home_mc {
            id
            name
        }
        opportunity {
            id
                    created_at
            title
            available_openings
            duration
            
            sub_product{
            name
            }
            programme {
            id
            short_name_display
            }
        }
        standards {
            option
        }
        }
        
        paging {
        current_page
        total_items
        total_pages
        }
    }
    }
    '''

    # Define the GraphQL endpoint
    url = 'https://gis-api.aiesec.org/graphql'

    # Define the headers with necessary authentication if required
    headers = {
        'Content-Type': 'application/json',
        'Authorization': '2293083fca0f1e5edfafc6d0cca9439a2363555438c60ca95658ca94461fd2f0'  # Add your access token here if required
    }

    # Send the GraphQL request
    response = requests.post(url, json={'query': query}, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract the JSON response
        json_data = response.json()
        
        # Extract the relevant data
        data = json_data['data']['allOpportunityApplication']['data']
        
        # Convert the data to a DataFrame
        df = pd.json_normalize(data)
        
        # Mapping of current column names to proper names
        column_mapping = {
            'id': 'ID',
            'status': 'Status',
            'created_at': 'Created At',
            'date_approved': 'Date Approved',
            'date_realized': 'Date Realized',
            'experience_start_date': 'Experience Start Date',
            'experience_end_date': 'Experience End Date',
            'date_approval_broken': 'Date Approval Broken',
            'nps_response_completed_at': 'NPS Response Completed At',
            'updated_at': 'Updated At',
            'standards': 'Standards',
            'person.id': 'Person ID',
            'person.home_mc.id': 'Person Home MC ID',
            'person.home_mc.name': 'Person Home MC Name',
            'person.home_lc.id': 'Person Home LC ID',
            'person.home_lc.name': 'Person Home LC Name',
            'host_lc.id': 'Host LC ID',
            'host_lc.name': 'Host LC Name',
            'home_mc.id': 'Home MC ID',
            'home_mc.name': 'Home MC Name',
            'opportunity.id': 'Opportunity ID',
            'opportunity.created_at': 'Opportunity Created At',
            'opportunity.title': 'Opportunity Title',
            'opportunity.available_openings': 'Available Openings',
            'opportunity.duration': 'Opportunity Duration',
            'opportunity.sub_product': 'Opportunity Sub Product',
            'opportunity.programme.id': 'Opportunity Programme ID',
            'opportunity.programme.short_name_display': 'Opportunity Programme Short Name',
            'opportunity.sub_product.name': 'Opportunity Sub Product Name'
        }
        # Rename columns using the mapping
        df.rename(columns=column_mapping, inplace=True)
        
        # Display the DataFrame
        st.sidebar.markdown('### Display Options')
        
        # Add multiselect dropdown for column selection
        selected_columns = st.sidebar.multiselect("Select Columns", df.columns.tolist(), default=["ID", "Opportunity ID", "Status"])
        
        # Add selectbox dropdown for Status selection
        selected_status = st.sidebar.selectbox("Select Status", sorted(df['Status'].unique()))
        
        # Filter the DataFrame based on selected status
        filtered_df = df[df['Status'] == selected_status]
        
        # Print the filtered DataFrame
        st.title("EP Status Changer")
        filtered_df = filtered_df[selected_columns]
        filtered_df['Change the Status'] = ""

        # Display the DataFrame
        st.dataframe(filtered_df.set_index(df.columns[0]), use_container_width=True)


if __name__ == "__main__":
    main()
