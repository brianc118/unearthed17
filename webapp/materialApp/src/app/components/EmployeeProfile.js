import React from 'react';
import {CardHeader} from 'material-ui/Card';
import FlatButton from 'material-ui/FlatButton';
const titleTextStyle = {
  fontSize: '1.5rem',
  color: '#FFF',
}
const subtitleTextStyle = {
  fontSize: '0.8rem',
  color: '#f2f2f2',
}
const EmployeeProfile = () => (
    <div className="employee-profile">
        <CardHeader
        titleStyle={titleTextStyle}
        className="profile-header"
        title="John Doe"
        subtitle="ID: 12345"
        subtitleStyle={subtitleTextStyle}
        avatar="../../img/default-dp.jpg"
        />
    </div>
);

export default EmployeeProfile;