import React from 'react';
import {Tabs, Tab} from 'material-ui/Tabs';
import SafeData from './overview/SafeData.js'
import ErrorData from './overview/ErrorData.js'
const styles = {
  headline: {
    fontSize: 24,
    paddingTop: 16,
    marginBottom: 12,
    fontWeight: 400,
  },
};
const circleSize = {
  margin: '1rem',
  height: '6rem',
  width: '6rem',
};
const inkStyle = {
    height: '3px',
    backgroundColor: '#4b4b4b',
}
const tabsStyle = {
    backgroundColor: 'none',
}
const tabStyle = {
    backgroundColor: 'none',
    color: '#666',
}


const tabview = () => (
        <Tabs className="overview-tabs" style={tabsStyle} inkBarStyle={inkStyle}>
            <Tab style={tabStyle} className="overview-tab" label="Overall">
            <div>
                <div className="float-left-fifty good-job">
                    <ul>
                        <li>Excellent Breaking</li>
                        <li>Great speed control</li>
                        <li>Seatbelt always on</li>
                        <li>No fatigued driving</li>
                    </ul>
                </div>
                <div className="float-left-fifty bad-job">
                    <ul>
                        <li>Harsh Acceleration</li>
                        <li>Fast cornering</li>
                    </ul>
                </div>
            </div>
            </Tab>
            <Tab style={tabStyle}  className="overview-tab" label="Safe Stats" >
            <div>
                <div className="flex-center safe-data">
                    <SafeData />
                </div>
            </div>
            </Tab>
                <Tab style={tabStyle}  className="overview-tab" label="Error Stats" >
            <div>
                <div className="flex-center safe-data">
                    <ErrorData />
                </div>
            </div>
            </Tab>
        </Tabs>
    );

export default tabview;