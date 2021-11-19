from django.shortcuts import render

usersList = [
    {
        'id': '1',
        'name': 'raptor'
    },
    {
        'id': '2',
        'name': 'ace'
    },
    {
        'id': '3',
        'name': 'dell'
    },
]


def projects(request):
    return render(request, 'projects/projects.html', {'users': usersList})


def project(request, id):
    projectObj = None
    for i in usersList:
        if i['id'] == id:
            projectObj = i

    if projectObj == None:
        return render(request, 'notfound.html')
    else:
        return render(request, 'projects/single-project.html', {'project': projectObj})
