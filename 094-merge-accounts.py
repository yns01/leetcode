from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        if not accounts:
            return []

        vertices = {account[i]: []
                    for account in accounts for i in range(1, len(account))}

        email_to_account_name = {}

        # Build a map mail to name
        for account in accounts:
            account_name = account[0]
            first_email = account[1]

            email_to_account_name[first_email] = account_name
            first_vertex = vertices.get(first_email)

            for i in range(2, len(account)):
                email = account[i]

                email_to_account_name[email] = account_name
                first_vertex.append(email)
                vertices[email].append(first_email)

        visited = set()

        # def visit(vertex, merged):
        #     visited.add(vertex)
        #     merged.append(vertex)

        #     for u in vertices[vertex]:
        #         if u not in visited:
        #             visit(u, merged)

        result = []
        for v in vertices:
            if v not in visited:
                merged = []
                stack = [v]
                visited.add(v)

                while stack:
                    vertex = stack.pop()
                    merged.append(vertex)

                    for u in vertices[vertex]:
                        if u not in visited:
                            stack.append(u)
                            visited.add(u)

                # visit(v, merged)
                result.append([email_to_account_name.get(v)] + sorted(merged))

        return result


accounts = [
    ['A', 'E1', 'E2', 'E3'],
    ['B', 'E4', 'E5'],
    ['A', 'E6'],
    ['C', 'E7'],
    ['A', 'E8', 'E1'],
    ['C', 'E9', 'E10', 'E11', 'E7']]

print(Solution().accountsMerge(accounts))
