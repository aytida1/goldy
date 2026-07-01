import mujoco

XML = "xml_folder/first.xml"

model = mujoco.MjModel.from_xml_path(XML)
data = mujoco.MjData(model)

while data.time < 1:
  mujoco.mj_step(model, data)
  print(data.geom_xpos)