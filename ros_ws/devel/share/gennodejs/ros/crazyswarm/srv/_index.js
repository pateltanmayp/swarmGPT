
"use strict";

let StartTrajectory = require('./StartTrajectory.js')
let Land = require('./Land.js')
let Stop = require('./Stop.js')
let SetGroupMask = require('./SetGroupMask.js')
let NotifySetpointsStop = require('./NotifySetpointsStop.js')
let UpdateParams = require('./UpdateParams.js')
let GoTo = require('./GoTo.js')
let Takeoff = require('./Takeoff.js')
let UploadTrajectory = require('./UploadTrajectory.js')

module.exports = {
  StartTrajectory: StartTrajectory,
  Land: Land,
  Stop: Stop,
  SetGroupMask: SetGroupMask,
  NotifySetpointsStop: NotifySetpointsStop,
  UpdateParams: UpdateParams,
  GoTo: GoTo,
  Takeoff: Takeoff,
  UploadTrajectory: UploadTrajectory,
};
