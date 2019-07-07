from IPython.display import display, Javascript

def nb_auto_export():
    display(Javascript("""{
const ip = IPython.notebook
if (ip) {
    ip.save_notebook()
    console.log('a')
    const s = `!python utils/notebook2script.py ${ip.notebook_name}`
    if (ip.kernel) { ip.kernel.execute(s) }
}
}"""))

def nb_auto_clear():
    display(Javascript("""{
const ip = IPython.notebook
if (ip) {
    console.log('a')
    const s = `!python utils/clear_nbcode.py ${ip.notebook_name}`
    if (ip.kernel) { ip.kernel.execute(s) }
}
location.reload(true);
}"""))
