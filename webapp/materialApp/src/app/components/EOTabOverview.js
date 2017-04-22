import React from 'react';
import { Line, Circle } from 'rc-progress';
import EOTabTabs from './EOTabTabs'
const circleSize = {
  margin: '1rem',
  height: '6rem',
  width: '6rem',
};

const Overview = () => (
    <div>
        <div className="tab-container">
            <div className="flex-center">
                <div style={circleSize}>
                    <p className="safe-percent-text"> 60 </p>
                    <Circle percent="60" strokeWidth="7" />
                </div>
                <div className="meta-info">
                    <p>John's driving score is <span>60/100</span></p>
                    <p>He has been on <span>7</span> trips, <br/>driven for <span>18 hours</span>, <br/>and covered about <span>765km</span></p>
                </div>
            </div>
            <div className="flex-center overview-padding">
                <div className="stat-box">
                    <p>safe</p>
                    <p><span>240</span></p>
                </div>
                <div className="stat-box">
                    <p>minor</p>
                    <p><span>12</span></p>
                </div>
                <div className="stat-box">
                    <p>critical</p>
                    <p><span>2</span></p>
                </div>
            </div>
            </div>
            <EOTabTabs />
    </div>

);

export default Overview;