import { Injectable } from '@angular/core';
import { Observable, of, delay } from 'rxjs';

export interface Hero {
  id: number;
  name: string;
}

@Injectable({
  providedIn: 'root'
})
export class HeroService {
  private heroes: Hero[] = [
    { id: 1, name: 'ずんだもん' },
    { id: 2, name: '四国めたん' },
    { id: 3, name: '春日部つむぎ' },
    { id: 4, name: '雨晴はう' },
    { id: 5, name: '波音リツ' },
  ];

  /**
   * ヒーロー一覧を取得（1秒のディレイ付き）
   */
  getHeroes(): Observable<Hero[]> {
    return of(this.heroes).pipe(delay(1000));
  }
}
