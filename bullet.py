import pybullet as p
import time
import pybullet_data
physicsClient = p.connect(p.GUI)#or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally
p.setGravity(0,0,-10)
planeId = p.loadURDF("plane.urdf")
startPos = [0,0,1]
startOrientation = p.getQuaternionFromEuler([0,0,0])
boxId = p.loadURDF("src/panther_description/urdf/panther.urdf",startPos, startOrientation)
#set the center of mass frame (loadURDF sets base link frame) startPos/Ornp.resetBasePositionAndOrientation(boxId, startPos, startOrientation)
# for i in range (10000):
while True:
    p.stepSimulation()
    p.setJointMotorControl2(
        bodyUniqueId=boxId, 
        jointIndex=2, 
        controlMode=p.VELOCITY_CONTROL,
        targetVelocity = 1
    )
    p.setJointMotorControl2(
        bodyUniqueId=boxId, 
        jointIndex=3, 
        controlMode=p.VELOCITY_CONTROL,
        targetVelocity = -1
    )
    p.setJointMotorControl2(
        bodyUniqueId=boxId, 
        jointIndex=4, 
        controlMode=p.VELOCITY_CONTROL,
        targetVelocity = 1
    )
    p.setJointMotorControl2(
        bodyUniqueId=boxId, 
        jointIndex=5, 
        controlMode=p.VELOCITY_CONTROL,
        targetVelocity = -1
    )
    time.sleep(1./240.)
cubePos, cubeOrn = p.getBasePositionAndOrientation(boxId)
print(cubePos,cubeOrn)
p.disconnect()
