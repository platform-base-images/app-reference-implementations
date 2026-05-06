package com.platform.api.controller;

import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;

import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api")
public class ItemController {

    @GetMapping("/health")
    public Map<String, String> health() {
        return Map.of("status", "ok", "service", "java-api");
    }

    @GetMapping("/items")
    public List<Map<String, Object>> listItems() {
        return List.of(
            Map.of("id", 1, "name", "item-1", "description", "First item"),
            Map.of("id", 2, "name", "item-2", "description", "Second item")
        );
    }

    @GetMapping("/items/{id}")
    public ResponseEntity<?> getItem(@PathVariable int id) {
        if (id < 1 || id > 2) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(
            Map.of("id", id, "name", "item-" + id, "description", "Item " + id)
        );
    }
}
