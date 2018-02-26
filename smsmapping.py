import plotly.plotly as py
from plotly.graph_objs import *
import plotly
from plotly.offline import plot
from twilio.rest import Client

account_sid = "ACfb32763b6b8d047b86df7534a70245e0"
auth_token = "f4e3fd3210a3e056d355d17eec5dad82"

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+918309594362",
    from_="+15024437038 ",
    body="An Accident has occures at the location: (12.9718° N, 79.1589° E)")


plotly.tools.set_credentials_file(username='aakashvarma18', api_key='tFCB65mxaAx9tFel2hDf')

mapbox_access_token = 'pk.eyJ1IjoiYWFrYXNoMTgiLCJhIjoiY2pka21xMzdzMDI1cTMzczN5MG9ic3c0eCJ9.-Jf_342u6cWFfCCAfWMJjQ'

lats=[12.9718] #12.9718° N, 79.1589° E
lons=[79.1589]

plots=[]
for i,j in zip(lats,lons):
    data = Data([
        Scattermapbox(
            lat=[str(i)],
            lon=[str(j)],
            mode='markers',
            marker=Marker(
                size=14
            ),
            text=['Accident has occured here, please reash the location as fast as possible'],
        )
    ])

    layout = Layout(
        autosize=True,
        hovermode='closest',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            center=dict(
                lat=12.9718,
                lon=79.1589
            ),
            pitch=0,
            zoom=20
        ),
    )
    fig = dict(data=data, layout=layout)
    print (fig)
plot(fig,"plot.html")