export class Golem{
  name: string;
  owner: string;
  golem_type: string;
  equipment: { [id: string] : { [id: string] : number; }; } = {};
}
