/**
 * In this file, we create a React component
 * which incorporates components provided by Material-UI.
 */
import React, {Component} from 'react';
import RaisedButton from 'material-ui/RaisedButton';
import Dialog from 'material-ui/Dialog';
import {
  blue500, blue700,
  purpleA200,
  grey100, grey300, grey400, grey500,
  white, darkBlack, fullBlack,
} from 'material-ui/styles/colors';
import FlatButton from 'material-ui/FlatButton';
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import MaterialNav from './components/MaterialNav.js'
import EmployeeProfile from './components/EmployeeProfile.js'
import EmployeeOverview from './components/EmployeeOverview.js'
const styles = {
  container: {
    textAlign: 'center',
  },
};

const muiTheme = getMuiTheme({
  palette: {
    primary1Color: blue500,
    primary2Color: blue700,
    primary3Color: grey400,
    accent1Color: purpleA200,
    accent2Color: grey100,
    accent3Color: grey500,
  },
});

class Main extends Component {
  constructor(props, context) {
    super(props, context);

    this.state = {
      open: false,
    };
  }

  handleRequestClose = () => {
    this.setState({
      open: false,
    });
  }

  handleTouchTap = () => {
    this.setState({
      open: true,
    });
  }

  render() {
    const standardActions = (
      <FlatButton
        label="Ok"
        primary={true}
        onTouchTap={this.handleRequestClose}
      />
    );

    return (
      <MuiThemeProvider muiTheme={muiTheme}>
        <div >
          <MaterialNav />
          <EmployeeProfile />
          <EmployeeOverview />
        </div>
      </MuiThemeProvider>
    );
  }
}

export default Main;
