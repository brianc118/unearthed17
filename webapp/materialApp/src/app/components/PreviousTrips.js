import React from 'react';
import {Card, CardActions, CardHeader, CardMedia, CardTitle, CardText} from 'material-ui/Card';
import FlatButton from 'material-ui/FlatButton';

const PreviousTrips = () => (
    <div>
  <Card className="trip-card">
    <CardMedia>
      <img src="img/map1.jpg" />
    </CardMedia>
    <CardTitle title="Trip to Maxwelton" subtitle="25/11/15" />
    <CardText>
      Toyota Hilux - 168km - 2hrs 15min
    </CardText>

  </Card>
  <Card className="trip-card">
    <CardMedia>
      <img src="img/map2.jpg" />
    </CardMedia>
    <CardTitle title="Trip to Longreach" subtitle="23/11/15" />
    <CardText>
      Toyota Hilux - 168km - 2hrs 15min
    </CardText>
  </Card>
  <Card className="trip-card">
    <CardMedia>
      <img src="img/map3.jpg" />
    </CardMedia>
    <CardTitle title="Trip to Emerald" subtitle="21/11/15" />
    <CardText>
      Toyota Hilux - 168km - 2hrs 15min
    </CardText>
  </Card>
  </div>
);
export default PreviousTrips;