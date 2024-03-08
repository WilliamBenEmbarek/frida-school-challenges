import frida

session = frida.attach("cat")
script = session.create_script("""
    rpc.exports.enumerateModules = () => {
        return Process.enumerateModules();
    };
""")
script.load()

print([m["name"] for m in script.exports_sync.enumerate_modules()])
