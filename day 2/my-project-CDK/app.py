from aws_cdk import core
from my_project.my_project_stack import MyProjectStack


app = core.App()
MyProjectStack(app, "my-project-CDK")

app.synth()
