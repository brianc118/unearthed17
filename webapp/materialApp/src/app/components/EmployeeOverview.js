import React from 'react';
import {Tabs, Tab} from 'material-ui/Tabs';
import Slider from 'material-ui/Slider';
import EOTabOverview from './EOTabOverview';
import Graphs from './Graphs';
import Trips from './PreviousTrips'
const styles = {
  headline: {
    fontSize: 24,
    paddingTop: 16,
    marginBottom: 12,
    fontWeight: 400,
  },
};

function handleActive(tab) {
  alert(`A tab with this route property ${tab.props['data-route']} was activated.`);
}
const inkStyle = {
    height: '5px',
}
const EmployeeOverview = () => (
  <Tabs className="employee-tabs" inkBarStyle={inkStyle}>
    <Tab className="employee-tab" label="Trips">
      <div>
        <Trips />
      </div>
    </Tab>
    <Tab className="employee-tab" label="Overview" >
      <div>
        <EOTabOverview />
      </div>
    </Tab>
    <Tab className="employee-tab" label="Breakdown" >
      <div>
        <Graphs />
      </div>
    </Tab>
  </Tabs>
);

export default EmployeeOverview;