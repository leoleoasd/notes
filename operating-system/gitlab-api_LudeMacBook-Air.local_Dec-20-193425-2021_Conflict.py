import gitlab
import random
token = "hiRQEvBcByiaJhokmBif"

gl = gitlab.Gitlab('http://172.21.14.74', private_token=token)

base_project = gl.projects.get('root/pintos')

# forked_project = base_project.forks.create({
#     'name': '19071125_pintos',
#     'path': '19071125_pintos',
#     'visibility': 'private'
# })

with open("users.csv") as f:
    users = [i.strip().split("\t") for i in f.readlines()]

# str = "abcdefghjkmnpqrstuvwxyz" + "abcdefghjkmnpqrstuvwxyz".upper() + "23456789"

# for i in users:
#     i.append("".join([random.choice(str) for i in range(0, 8)]))

# print(users)

# with open("users.csv", "w") as f:
#     f.write("\n".join("\t".join(i) for i in users))

# exit(0)

gl_users = {}

for u in users:
    # try:
    #     print(gl.users.list(username=u[1])[0].delete())
    # except IndexError:
    #     pass

    # gl_users[u[0]] = gl.users.create({'email': f"{u[1]}@bjut.edu.cn",
    # 'password': u[2],
    # 'username': u[1],
    # 'skip_confirmation': True,
    # 'name': f'{u[0]} {u[1]}'})

    gl_user = gl.users.list(username=u[1])[0]
    print(gl_user)
    gl_user.password = "QWFAERErgfiueorfq33tfaisd79yq34o"
    gl_user.save()
    # break

    # base_project.forks.create({
    #     'name': f"{u[0]} {u[1]} pintos",
    #     'path': f"{u[1]}_pintos",
    #     'visibility': 'private',
    # })

    # forked_project = gl.projects.list(search=f"{u[1]}_pintos")[0]

    # try:
    #     forked_project.protectedbranches.delete('master')
    # except Exception:
    #     pass
    # exit(0)

    # print(forked_project)

    # forked_project.members.create({'user_id': gl_user.id, 'access_level':
    #                              gitlab.DEVELOPER_ACCESS})
    # exit(0)

# exit(0)


# # base_project.fork()