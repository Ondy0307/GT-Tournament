from testUtils import getJws, requestExpect
from copy import deepcopy

create = {
    "permission": "assignedRole.read",
    "generatedRoleId": 1,
    "gameId": None,
    "eligible": False,
}

result = deepcopy(create)
result["generatedRolePermissionId"] = int

class Test:
    def __init__(self):
        self.jws = getJws("114316488057882015")

    def run(self):
        res = requestExpect.post("/backend/generatedRolePermission/create", create, 201,
            {
                "Authorization":f"Bearer {self.jws}",
            }, result
        )
        generatedRolePermissionId = res["generatedRolePermissionId"]
        result["generatedRolePermissionId"] = generatedRolePermissionId
        requestExpect.get(f"/backend/generatedRolePermission/{generatedRolePermissionId}/", 200, {},  result)

    def __del__(self):
        pass
