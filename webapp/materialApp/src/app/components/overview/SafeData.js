import React from 'react';
import {Table, TableBody, TableHeader, TableHeaderColumn, TableRow, TableRowColumn} from 'material-ui/Table';

const SafeData = () => (
    <div className="safe-data">
        <div className="stat-box">
            <p>Never sped</p>
            <p><span>13</span></p>
        </div>
        <div className="stat-box">
            <p>Seat belt on</p>
            <p><span>14</span></p>
        </div>
        <div className="stat-box">
            <p>Smooth Stops</p>
            <p><span>875</span></p>
        </div>
        <div className="stat-box">
            <p>Safe Corners</p>
            <p><span>240</span></p>
        </div>
        <div className="stat-box">
            <p>Smooth takeoffs</p>
            <p><span>426</span></p>
        </div>
        <div className="stat-box">
            <p>Smooth Stops</p>
            <p><span>875</span></p>
        </div>
    </div>
);
export default SafeData;