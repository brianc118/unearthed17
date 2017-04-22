import React from 'react';
import {Table, TableBody, TableHeader, TableHeaderColumn, TableRow, TableRowColumn} from 'material-ui/Table';

const SafeData = () => (
    <div className="safe-data">
        <h2>Critical Errors</h2>
        <div className="stat-box">
            <p>Speeding > 10km/h</p>
            <p><span>2</span></p>
        </div>
        <div className="stat-box">
            <p>Use of Phone</p>
            <p><span>4</span></p>
        </div>
        <h2>Minor Errors</h2>
        <div className="stat-box">
            <p>Fast Acceleration</p>
            <p><span>875</span></p>
        </div>
        <div className="stat-box">
            <p>Seat Belt Off 10sec</p>
            <p><span>240</span></p>
        </div>
        <div className="stat-box">
            <p>Harsh Corner</p>
            <p><span>426</span></p>
        </div>
    </div>
);
export default SafeData;