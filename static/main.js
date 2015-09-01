function render(){
    var vars = document.getElementById("vars").value;
    var tmpl = document.getElementById("tmpl").value;
    superagent
        .post('../api/render')
        .send({vars: vars, tmpl: tmpl})
        .end(function(err, res){
            document.getElementById("result").innerHTML = res.text;
        })
}
